#!/usr/bin/env python3
"""
Robots Exposure Check (read-only)

Purpose:
- Fetch robots.txt
- Parse User-agent and Disallow paths
- Check whether disallowed paths are still publicly accessible
- Flag potentially sensitive path patterns

Use only on assets you own or are explicitly authorized to assess.
No exploitation or intrusive actions are performed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Dict, List, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

SENSITIVE_PATH_HINTS = [
    "admin",
    "backup",
    "private",
    "internal",
    "secret",
    "config",
    "db",
    "dev",
    "staging",
    "test",
    "api",
]


@dataclass
class PathCheck:
    user_agent: str
    path: str
    url: str
    status: int
    sensitive_hint: bool


@dataclass
class ExposureReport:
    target: str
    robots_url: str
    timestamp_utc: str
    robots_http_status: int
    tested_paths: int
    accessible_paths: List[PathCheck]
    warnings: List[str]


def normalize_target(raw: str) -> str:
    raw = raw.strip()
    if not raw:
        raise ValueError("Target cannot be empty")

    parsed = urlparse(raw)
    if not parsed.scheme:
        raw = f"https://{raw}"
        parsed = urlparse(raw)

    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("Provide a valid http/https target")

    return f"{parsed.scheme}://{parsed.netloc}"


def http_get(url: str, timeout: int):
    req = Request(
        url,
        method="GET",
        headers={
            "User-Agent": "RobotsExposureCheck/1.0 (+defensive-read-only)",
            "Accept": "*/*",
        },
    )
    return urlopen(req, timeout=timeout)


def fetch_robots(robots_url: str, timeout: int) -> Tuple[int, str]:
    with http_get(robots_url, timeout) as resp:
        status = getattr(resp, "status", 200)
        body = resp.read().decode("utf-8", errors="replace")
        return status, body


def parse_robots_disallow_paths(content: str) -> List[Tuple[str, str]]:
    current_agents: List[str] = []
    disallow_entries: List[Tuple[str, str]] = []

    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        if "#" in line:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()

        if key == "user-agent":
            if value:
                current_agents.append(value)
            continue

        if key == "disallow":
            if not current_agents:
                current_agents = ["(unspecified)"]
            for ua in current_agents:
                disallow_entries.append((ua, value))
            continue

        if key in {"allow", "sitemap", "crawl-delay", "host"}:
            if key in {"allow", "sitemap"}:
                current_agents = current_agents

    return disallow_entries


def robots_pattern_to_path(disallow_value: str) -> str:
    value = disallow_value.strip()
    if not value:
        return ""

    value = value.replace("*", "")
    value = value.rstrip("$")

    if not value.startswith("/"):
        value = "/" + value

    value = re.sub(r"//+", "/", value)
    return value


def is_sensitive_hint(path: str) -> bool:
    lowered = path.lower()
    return any(hint in lowered for hint in SENSITIVE_PATH_HINTS)


def check_path_access(base_url: str, path: str, timeout: int) -> int:
    url = urljoin(base_url, path)
    try:
        with http_get(url, timeout) as resp:
            return getattr(resp, "status", 200)
    except HTTPError as exc:
        return exc.code
    except Exception:
        return 0


def run_check(target: str, timeout: int, max_paths: int) -> ExposureReport:
    robots_url = urljoin(target, "/robots.txt")
    warnings: List[str] = []

    try:
        robots_status, robots_content = fetch_robots(robots_url, timeout)
    except HTTPError as exc:
        return ExposureReport(
            target=target,
            robots_url=robots_url,
            timestamp_utc=datetime.now(timezone.utc).isoformat(),
            robots_http_status=exc.code,
            tested_paths=0,
            accessible_paths=[],
            warnings=[f"robots.txt returned HTTP {exc.code}"],
        )
    except URLError as exc:
        return ExposureReport(
            target=target,
            robots_url=robots_url,
            timestamp_utc=datetime.now(timezone.utc).isoformat(),
            robots_http_status=0,
            tested_paths=0,
            accessible_paths=[],
            warnings=[f"Network error while fetching robots.txt: {exc.reason}"],
        )

    disallowed = parse_robots_disallow_paths(robots_content)
    if not disallowed:
        warnings.append("No Disallow directives found")

    unique_pairs: List[Tuple[str, str]] = []
    seen = set()
    for ua, raw_path in disallowed:
        normalized_path = robots_pattern_to_path(raw_path)
        if not normalized_path:
            continue
        key = (ua, normalized_path)
        if key not in seen:
            seen.add(key)
            unique_pairs.append(key)

    if len(unique_pairs) > max_paths:
        warnings.append(
            f"Path list truncated from {len(unique_pairs)} to {max_paths} checks"
        )
        unique_pairs = unique_pairs[:max_paths]

    accessible: List[PathCheck] = []
    for ua, path in unique_pairs:
        url = urljoin(target, path)
        status = check_path_access(target, path, timeout)
        if 200 <= status < 400:
            accessible.append(
                PathCheck(
                    user_agent=ua,
                    path=path,
                    url=url,
                    status=status,
                    sensitive_hint=is_sensitive_hint(path),
                )
            )

    if accessible:
        warnings.append(
            "Some disallowed paths are publicly reachable. This may be intentional and is not proof of a vulnerability by itself."
        )

    high_risk = [item for item in accessible if item.sensitive_hint]
    if high_risk:
        warnings.append(
            f"{len(high_risk)} reachable paths include sensitive naming hints; review access controls."
        )

    return ExposureReport(
        target=target,
        robots_url=robots_url,
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
        robots_http_status=robots_status,
        tested_paths=len(unique_pairs),
        accessible_paths=accessible,
        warnings=warnings,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only check for reachable paths listed in robots.txt"
    )
    parser.add_argument("target", help="Target domain or URL (authorized scope only)")
    parser.add_argument("--timeout", type=int, default=8, help="Request timeout seconds")
    parser.add_argument(
        "--max-paths",
        type=int,
        default=40,
        help="Maximum number of Disallow paths to test (default: 40)",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    args = parser.parse_args()

    try:
        target = normalize_target(args.target)
    except ValueError as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2

    report = run_check(target, args.timeout, args.max_paths)

    if args.json:
        print(json.dumps(asdict(report), indent=2))
        return 0

    print("Robots Exposure Check")
    print(f"Target: {report.target}")
    print(f"robots URL: {report.robots_url}")
    print(f"Timestamp (UTC): {report.timestamp_utc}")
    print(f"robots.txt HTTP status: {report.robots_http_status}")
    print(f"Disallow paths tested: {report.tested_paths}")
    print()

    if report.accessible_paths:
        print("Reachable disallowed paths:")
        for item in report.accessible_paths:
            risk = "SENSITIVE_HINT" if item.sensitive_hint else "normal"
            print(
                f"- [{item.status}] ua={item.user_agent} path={item.path} risk={risk} url={item.url}"
            )
    else:
        print("No disallowed paths were reachable (2xx/3xx) in tested set.")

    if report.warnings:
        print()
        print("Warnings:")
        for warning in report.warnings:
            print(f"- {warning}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

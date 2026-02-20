"""
Simple API built with Python's built-in http.server module.

Endpoints:
  GET /          → Plain text greeting
  GET /data      → JSON sample dataset
  GET /status    → API status check
  GET /info      → API metadata
  GET /*         → 404 Not Found
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# ── Configuration ────────────────────────────────────────────────────────────
HOST = "localhost"
PORT = 8000


# ── Request Handler ──────────────────────────────────────────────────────────
class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handles incoming HTTP requests and routes them to the correct method."""

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _send_text(self, status: int, message: str) -> None:
        """Send a plain-text response."""
        body = message.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status: int, data: dict) -> None:
        """Serialize *data* to JSON and send it as a response."""
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # ── Suppress default request logging (optional – comment out to restore) ──
    def log_message(self, fmt, *args):
        print(f"  [{self.address_string()}] {fmt % args}")

    # ── GET routing ───────────────────────────────────────────────────────────

    def do_GET(self) -> None:
        """Route GET requests to the appropriate handler."""

        routes = {
            "/":       self._handle_root,
            "/data":   self._handle_data,
            "/status": self._handle_status,
            "/info":   self._handle_info,
        }

        handler = routes.get(self.path)

        if handler:
            handler()
        else:
            self._handle_not_found()

    # ── Endpoint handlers ─────────────────────────────────────────────────────

    def _handle_root(self) -> None:
        """GET /  →  plain-text greeting."""
        self._send_text(200, "Hello, this is a simple API!")

    def _handle_data(self) -> None:
        """GET /data  →  sample JSON dataset."""
        payload = {
            "name": "John",
            "age":  30,
            "city": "New York",
        }
        self._send_json(200, payload)

    def _handle_status(self) -> None:
        """GET /status  →  API health check."""
        self._send_json(200, {"status": "OK"})

    def _handle_info(self) -> None:
        """GET /info  →  API metadata."""
        payload = {
            "version":     "1.0",
            "description": "A simple API built with http.server",
        }
        self._send_json(200, payload)

    def _handle_not_found(self) -> None:
        """Catch-all for undefined endpoints → 404."""
        self._send_json(404, {
            "error":   "Not Found",
            "message": f"Endpoint '{self.path}' does not exist.",
        })


# ── Entry point ───────────────────────────────────────────────────────────────

def run(host: str = HOST, port: int = PORT) -> None:
    server = HTTPServer((host, port), SimpleAPIHandler)
    print(f"🚀  Server running at http://{host}:{port}")
    print("    Press Ctrl+C to stop.\n")
    print("  Available endpoints:")
    print(f"    GET http://{host}:{port}/        → greeting text")
    print(f"    GET http://{host}:{port}/data    → sample JSON")
    print(f"    GET http://{host}:{port}/status  → health check")
    print(f"    GET http://{host}:{port}/info    → API metadata")
    print()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋  Server stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    run()

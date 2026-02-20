"""
Simple API using Python's http.server module.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Simple HTTP request handler."""

    def _set_headers(self, status=200, content_type="text/plain"):
        """Set response headers."""
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self._set_headers(content_type="application/json")
            data = {
                "name": "John",
                "age": 30,
                "city": "New York",
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            # IMPORTANT: plain text "OK"
            self._set_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self._set_headers(content_type="application/json")
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self._set_headers(status=404)
            self.wfile.write(b"Endpoint not found")


def run():
    """Start HTTP server on port 8000."""
    server = HTTPServer(("", 8000), SimpleAPIHandler)
    server.serve_forever()


if __name__ == "__main__":
    run()

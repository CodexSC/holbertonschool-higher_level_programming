"""
Simple API built with Python's built-in http.server module.

Endpoints:
  GET /      -> "Hello, this is a simple API!" (plain text)
  GET /data  -> {"name": "John", "age": 30, "city": "New York"}
  GET /status -> {"status": "OK"}
  GET /info  -> {"version": "1.0", "description": "A simple API built with http.server"}
  GET /*     -> 404 "Endpoint not found"
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(200, data)

        elif self.path == "/status":
            self._send_json(200, {"status": "OK"})

        elif self.path == "/info":
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send_json(200, data)

        else:
            self._send_json(404, {"error": "Endpoint not found"})

    def _send_json(self, status_code, data):
        """Helper to send a JSON response."""
        body = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run():
    server = HTTPServer((HOST, PORT), SimpleAPIHandler)
    print(f"Server running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":

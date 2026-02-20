"""
A simple RESTful-like API using Python's built-in http.server
module.

Features:
- Serves basic text responses.
- Serves JSON data at specific endpoints.
- Handles "/", "/data", "/status", "/info".
- Returns 404 JSON for undefined endpoints.

Usage:
    python task_03_http_server.py

Test with:
    http://localhost:8000/
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    HTTP request handler for a simple API.

    Overrides do_GET to route endpoints.
    """

    def _set_headers(
        self,
        status_code=200,
        content_type="text/plain",
    ):
        """
        Set HTTP response headers.

        Args:
            status_code (int):
                HTTP status code (default 200).
            content_type (str):
                Response content type.
        """
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        """
        Handle GET requests.

        Supported endpoints:
        - "/"
        - "/data"
        - "/status"
        - "/info"
        """
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self._set_headers(
                content_type="application/json"
            )
            data = {
                "name": "John",
                "age": 30,
                "city": "New York",
            }
            self.wfile.write(
                json.dumps(data).encode("utf-8")
            )

        elif self.path == "/status":
            self._set_headers(
                content_type="application/json"
            )
            status = {"status": "OK"}
            self.wfile.write(
                json.dumps(status).encode("utf-8")
            )

        elif self.path == "/info":
            self._set_headers(
                content_type="application/json"
            )
            info = {
                "version": "1.0",
                "description": (
                    "A simple API built with "
                    "http.server"
                ),
            }
            self.wfile.write(
                json.dumps(info).encode("utf-8")
            )

        else:
            self._set_headers(
                status_code=404,
                content_type="application/json",
            )
            error = {"error": "Endpoint not found"}
            self.wfile.write(
                json.dumps(error).encode("utf-8")
            )


def run(
    server_class=HTTPServer,
    handler_class=SimpleAPIHandler,
    port=8000,
):
    """
    Start the HTTP server.
    """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(
        f"Starting simple API server on port {port}..."
    )
    httpd.serve_forever()


if __name__ == "__main__":
    run()

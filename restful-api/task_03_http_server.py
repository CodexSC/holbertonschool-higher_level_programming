"""
A simple RESTful-like API using Python's built-in http.server module.

Features:
- Serves basic text responses.
- Serves JSON data at specific endpoints.
- Handles multiple endpoints: "/", "/data", "/status", "/info".
- Returns a 404 JSON response for undefined endpoints.

Usage:
    python task_03_http_server.py

Then visit in a browser or use curl:
    http://localhost:8000/
    http://localhost:8000/data
    http://localhost:8000/status
    http://localhost:8000/info
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    HTTP request handler class for a simple API.

    Inherits from BaseHTTPRequestHandler and overrides do_GET
    to handle GET requests for specific endpoints.
    """

    def _set_headers(self, status_code=200, content_type="text/plain"):
        """
        Helper method to set HTTP headers for responses.

        Args:
            status_code (int): HTTP status code (default 200 OK).
            content_type (str): Content-Type of the response (default "text/plain").
        """
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()


    def do_GET(self):
        """
        Handle GET requests.

        Supports the following endpoints:
        - "/"      : Returns a simple text message.
        - "/data"  : Returns a sample JSON dataset.
        - "/status": Returns API status in JSON.
        - "/info"  : Returns API information in JSON.
        Any other endpoint returns a 404 JSON error.
        """
        if self.path == "/":
            # Root endpoint returns simple text
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # JSON data endpoint
            self._set_headers(content_type="application/json")
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            # API status endpoint
            self._set_headers(content_type="application/json")
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode("utf-8"))

        elif self.path == "/info":
            # API info endpoint
            self._set_headers(content_type="application/json")
            info = {
                "version": "1.0",
                "description": (
                    "A simple API built with http.server"
                )
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            # Undefined endpoints return 404 error
            self._set_headers(status_code=404, content_type="application/json")
            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Start the HTTP server.

    Args:
        server_class: Class used to create the HTTP server (default HTTPServer).
        handler_class: Request handler class (default SimpleAPIHandler).
        port (int): Port number for the server to listen on (default 8000).
    """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting simple API server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

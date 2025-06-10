#!/usr/bin/python3
"""
Module: task_03_http_server.py

This module implements a basic HTTP server using Python's
built-in http.server module.
It provides a few predefined endpoints that demonstrate
how to handle HTTP GET requests and return plain text or JSON responses.

Endpoints:
- `/`        → Returns a simple text response.
- `/data`    → Returns sample JSON data.
- `/status`  → Returns a JSON object indicating the API status.
- `/info`    → Returns version and description information.
Any other endpoint returns a 404 Not Found message.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    """
    Custom request handler for the HTTP server.

    Handles GET requests and routes to specific endpoints:
    - "/"        → Returns plain text greeting.
    - "/data"    → Returns sample JSON data.
    - "/status"  → Returns JSON status.
    - "/info"    → Returns JSON version and description.
    """

    def do_GET(self):
        """
        Handle GET requests based on the requested path.

        Responds with appropriate content type and body.
        Sends 404 error for undefined routes.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data_set = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data_set)
            self.wfile.write(json_data.encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data_dict = {"status": "OK"}
            json_dict = json.dumps(data_dict)
            self.wfile.write(json_dict.encode())

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data_info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_info = json.dumps(data_info)
            self.wfile.write(json_info.encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8000), Handler)
    httpd.serve_forever()

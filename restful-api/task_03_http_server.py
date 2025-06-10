from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello from HTTP server".encode())

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data_set = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data_set)
            self.wfile.write(json_data.encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data_dict = {"status": "OK"}
            json_dict = json.dumps(data_dict)
            self.wfile.write(json_dict.encode())

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data_info = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            json_info = json.dumps(data_info)
            self.wfile.write(json_info.encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())

httpd = HTTPServer(('localhost', 8000), Handler)
httpd.serve_forever()

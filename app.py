from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            message = "Hello from Docker!"
        elif self.path == "/api":
            message = '{"message": "Hello from the API!"}'
        else:
            message = "Not Found"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())


server = HTTPServer(("0.0.0.0", 8080), Handler)

print("Python app running on port 8080")

server.serve_forever()
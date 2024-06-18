import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Check if the requested path is a directory
        if self.path.endswith('/'):
            self.path += 'index.html'
        
        # Check if the requested path exists
        if not os.path.exists(self.translate_path(self.path)):
            # If the requested path doesn't exist, try appending .html
            if not self.path.endswith('.html'):
                self.path += '.html'
        
        # Serve the file
        return super().do_GET()

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
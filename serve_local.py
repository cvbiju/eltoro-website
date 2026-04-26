import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "public"

class NetlifyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # translate_path resolves self.path relative to the directory parameter we passed
        path = self.translate_path(self.path)
        
        # If the requested path is not a file or directory, check if .html exists
        if not os.path.exists(path):
            if os.path.exists(path + '.html'):
                # modify the request path to append .html
                self.path += '.html'
                
        return super().do_GET()

with socketserver.TCPServer(("", PORT), NetlifyHandler) as httpd:
    print(f"Serving HTTP on port {PORT} (http://localhost:{PORT}/) with Netlify clean URL support...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

#!env python3
# -*- coding: utf-8 -*-
import threading
from socketserver import ThreadingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer

class TestServer(BaseHTTPRequestHandler):
    def handle_headers(self):
        for k, v in self.headers.items():
            print(k , ":" ,v)
            self.rfile.close()
            self.send_response(200)
            self.end_headers()
            
    def do_GET(self):
        self.handle_headers()
        self.wfile.write(bytes(self.path, "utf-8"))
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.handle_headers()
        self.wfile.write(post_data)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

httpd = ThreadedHTTPServer(("0.0.0.0", 8000), TestServer)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()

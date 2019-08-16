#!env python3
# -*- coding: utf-8 -*-
import threading
from socketserver import ThreadingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer
from multiprocessing import Process

import urllib.parse
import urllib.request

import http.client

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

def run():
    httpd = ThreadedHTTPServer(("0.0.0.0", 8000), TestServer)
    httpd.allow_reuse_address = True
    try:
        httpd.handle_request()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
 
# urlopen
import urllib.request
res = urllib.request.urlopen('http://impress.co.jp/')
htmlbuf = res.read(300)
res.close()
print(htmlbuf)

# urlretrieve
import urllib.request
url = "http://chart.apis.google.com/chart?cht=qr&chs=300x300&chl=hello"
with urllib.request.urlopen(url) as img:
    with open("qrcode.png", 'wb') as file:
        file.write(img.read())

# jsonデータ
import urllib.request
import json
url = 'https://www.googleapis.com/books/v1/volumes?q=id:JPNhCAAAQBAJ'
response = urllib.request.urlopen(url)
content = json.loads(response.read().decode('utf-8'))
print(content)

# request
p = Process(target=run)
p.start()
url = "http://localhost:8000/test"
buf = "Hello World".encode()
req = urllib.request.Request(url, buf)
with urllib.request.urlopen(req) as res:  
    print(res.read().decode())
p.join()

# add_header
p = Process(target=run)
p.start()
url = "http://localhost:8000"
req = urllib.request.Request(url)
req.add_header("X-MY-HEADER", "python_standard_library")
with urllib.request.urlopen(req) as res:
    html = res.read().decode("utf-8")
p.join()

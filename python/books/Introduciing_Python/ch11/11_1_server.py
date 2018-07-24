#!env python3
from datetime import datetime
import socket

address = ('localhost', 6790)
max_size = 1000
print('Starting the server at', datetime.now())
print('Waiting for a client to call.')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(address)
server.listen(5)

client, addr = server.accept()
data = client.recv(max_size)
print('At', datetime.now(), client, 'said', data)
if data == b'time':
    client.sendall(str(datetime.now()).encode('utf-8'))

client.close()
server.close()

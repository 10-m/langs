#!env python3
# -*- coding: utf-8 -*-
from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime

def time():
    return(datetime.now())

server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(time, "time")
server.serve_forever()

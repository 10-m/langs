#!env python3
# -*- coding: utf-8 -*-

import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")

result = proxy.time()
print("result:{}".format(result))


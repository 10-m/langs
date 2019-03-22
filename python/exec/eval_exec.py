#!env python3
# -*- coding: utf-8 -*-

# eval
print(eval("3 + 10"))

num = 15
print(eval("num * 2"))

print(eval("num * 2", {"num": 20}))

# exec
exec("x = 3 * 4") 
print(x)

f = open('./infile.py', encoding="utf8")
cmd = f.read()
exec(cmd)

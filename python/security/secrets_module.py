#!env python3
# -*- coding: utf-8 -*-
import secrets
import string

chars = string.ascii_letters + string.digits
while True:
    passwd = ''.join(secrets.choice(chars) for i in range(8))
    chk1 = any(c.islower() for c in passwd)
    chk2 = any(c.isupper() for c in passwd)
    chk3 = len([c for c in passwd if c.isdigit()]) >= 2
    if chk1 and chk2 and chk3:
        break
print(passwd)

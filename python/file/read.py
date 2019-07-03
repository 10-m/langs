#!env python3
# -*- coding: utf-8 -*-
import re

file = 'read.py';
with open(file, 'r') as fd:
    for line in fd:
        line = re.sub('\r?\n?$', '', line)
        print(line)

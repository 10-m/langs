#!env python3
# -*- coding: utf-8 -*-
from time import time
from datetime import datetime

def get_now():
    return datetime.now()

def get_this_month():
    return get_now().month

def add_time(addtion=3600):
    return time() + addtion

#!env python3
# -*- coding: utf-8 -*-

import os
import pickle

file = "pickle.dat"

data = {"apple":3, "orange":2}
with open(file, mode="wb") as f:
    pickle.dump(data, f)

if os.path.exists(file):
    with open(file, mode='rb') as f:
        obj = pickle.load(f)
        print(obj)
    os.remove(file)

pickled = pickle.dumps(data) 
print(f'{pickled}')
print(f'{pickle.loads(pickled)}')

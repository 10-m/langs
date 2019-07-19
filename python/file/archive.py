#!env python3
# -*- coding: utf-8 -*-

import os
import shutil
import pathlib
import zipfile
import glob

# make_archive
os.mkdir('tmp')
shutil.make_archive('tmp', 'zip', base_dir='./tmp')
os.rmdir('tmp')

# unpack_archive
shutil.unpack_archive('tmp.zip', './', 'zip')
os.rmdir('tmp')
os.remove('tmp.zip')

with zipfile.ZipFile("work.zip", "w") as zf:
    for f in glob.glob('*.py'):
        zf.write(f)

with zipfile.ZipFile("work.zip", "r") as zf:
    for f in zf.namelist():
        data = zf.read(f)
        print('{}:{}'.format(f, len(data)))
os.remove('work.zip')

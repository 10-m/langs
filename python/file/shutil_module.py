#!env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from shutil import copy2, copytree, rmtree
from subprocess import getoutput

# copy
copy2(__file__, 'hoge.py')
print(getoutput('ls -l hoge.py'))

Path('input').mkdir(parents=True, exist_ok=True)
p = Path('newdir')
if p.exists():
    # delte dir
    rmtree('newdir')

# copy dir
copytree('input', 'newdir')
print(getoutput('ls -lR newdir'))

Path('input').rmdir()
Path('newdir').rmdir()
Path('hoge.py').unlink()

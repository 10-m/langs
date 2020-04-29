#!env python3
# -*- coding: utf-8 -*-
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path
from subprocess import getoutput

# ZIPファイルの作成
with ZipFile('newsample.zip', 'w') as f:
    f.write(__file__, compress_type=ZIP_DEFLATED)

# ZIPファイルの確認
with ZipFile('newsample.zip') as f:
    f.printdir()

# ZIPファイル解凍
with ZipFile('newsample.zip') as f:
    f.extractall('tmp')
print(getoutput('ls -lR tmp'))

Path('newsample.zip').unlink()
Path('tmp/' + __file__).unlink()
Path('tmp/').rmdir()

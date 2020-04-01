#!env python3
# -*- coding: utf-8 -*-

from pathlib import Path

this_file = Path(__file__)
print('this_file:', this_file)

# check
print('this_file.exists():', this_file.exists())
print('this_file.is_file():', this_file.is_file())
print('this_file.is_dir():', this_file.is_dir())

# joinpath
script_dir = this_file.parent
p = script_dir.joinpath('tmp', 'new_dir')

# mkdir
print(p, p.exists())
p.mkdir(parents=True, exist_ok=True)  # 存在していても作成
print(p, p.exists())

new_p = p.joinpath('text.txt')
print(new_p)

# info
print('new_p.name:', new_p.name)  # ファイル名の取得
print('new_p.suffix:', new_p.suffix)  # 拡張子の取得
print('new_p.stem:', new_p.stem)  # ファイル名の拡張子以外の部分の取得
print('new_p.parts:', new_p.parts)  # パスを分解したものの取得
print('new_p.parent:', new_p.parent)  # 親ディレクトリーの取得

# full path
this_path = this_file.resolve()
print(this_path)

# write
new_p.write_text('TEXT')

# read
print(new_p.read_text())

# unlink
new_p.unlink()

# glob
for f in script_dir.glob('*'):
    print('-', f)
for f in script_dir.glob('**/*'):
    print('-', f)

# rmdir
p.rmdir()
p.parent.rmdir()

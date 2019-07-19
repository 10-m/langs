#!env python3
# -*- coding: utf-8 -*-
import os
import sys
import shutil
import pathlib
import tempfile

# dirname
dirname = os.path.dirname(__file__)

# join
path = os.path.join(dirname, "sample.txt")
print(path)

# split
print(os.path.split("/hello/world/python.txt"))

# basename
print(os.path.basename("/hello/world/python.txt"))

# splitext
print(os.path.splitext("/hello/world/python.txt"))

# join
print(os.sep.join(["dir1", "dir2", "dir3"]))
print(os.path.join("/home/user1", "/home/user2"))

# normpath()
print(os.path.normpath('/A/B/C/../D'))

# isfile
print(os.path.isfile(sys.argv[0]))

# isdir
print(os.path.isdir(sys.argv[0]))

# exists
print(os.path.exists(sys.argv[0]))

# mkdir and rmdir
os.mkdir('tmp')
print(os.path.isdir('tmp'))
os.rmdir('tmp')
print(os.path.isdir('tmp'))

# makedirs and removedirs
os.makedirs('a/b/c')
print(os.path.isdir('a/b/c'))
os.removedirs('a/b/c')
print(os.path.isdir('a/b/c'))

# remdtree
os.makedirs('a/b/c')
print(os.path.isdir('a/b/c'))
shutil.rmtree('a')
print(os.path.isdir('a'))

# touch and remove
pathlib.Path("test.txt").touch()
print(os.path.isfile('test.txt'))
os.remove('test.txt')
print(os.path.isfile('test.txt'))

# getcwd and chrid
current = os.getcwd()
print(current)
os.chdir('/tmp')
print(os.getcwd())
os.chdir(current)

# listdir
print(os.listdir('.'))

# scandir
for f in os.scandir('.'):
    print('---')
    print(f.name)
    print(f.path)
    print(f.inode())
    print(f.is_dir())
    print(f.is_file())
    print(f.is_symlink())
    stat = f.stat()
    print('{:o}'.format(stat.st_mode))
    print(stat.st_uid)
    print(stat.st_gid)
    print(stat.st_size)
    print(stat.st_mtime)
    
# rename
pathlib.Path("test.txt").touch()
os.rename("test.txt", "test2.txt")

# move
shutil.move("test2.txt", "test3.txt")
print(os.path.isfile('test3.txt'))
os.remove('test3.txt')

# mkstemp
fd, name = tempfile.mkstemp(prefix="python", suffix="test")
print(fd, name)
f = os.fdopen(fd, 'w')
f.close()

# auto remove
with tempfile.TemporaryFile(mode='w+t') as f:
    f.write("Hello Python")
    f.seek(0)
    print(f.read())

# copy
pathlib.Path("test.txt").touch()
shutil.copy("test.txt", "test2.txt")
os.remove('test.txt')
os.remove('test2.txt')

# which
print(shutil.which('ls'))
print(os.environ.get('PATH', os.defpath))

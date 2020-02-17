#!env python3
# -*- coding: utf-8 -*-

# 任意個数の位置引数
def func(*args):
    print(args)  # ('hello', 'world')
    for arg in args:
        print(arg, end=' ')
    print()
func('hello', 'world')

# 変数のアンパック
def func(*args):
    print(*args)
func('hello', 'world')

# 任意個数のキーワード引数
def func(*args, **kwargs):
    print(args, kwargs)
func(1, 2, 3, abc=1, xyz='xyz')

# 辞書からキーワード変数へ
def func(*args, **kwargs):
    print(*args, **kwargs)
func(1, 2, 3, sep='-')

# ラムダ式
func = lambda a, b: a + b
print(func(1, 2))

# ドキュメンテーション文字列
def add(a, b):
    """Add a and b.

    `add(a, b)` is same as `a + b`.
    """
    return a + b
print(add.__doc__)

#!env python3
# -*- coding: utf-8 -*-

def show_func_name(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, 'を実行します')
        return func(*args, **kwargs)
    return wrapper


def talk(message):
    print(message)

new_talk = show_func_name(talk)
new_talk('ごきげんよう')

# @による実行
@show_func_name
def talk(message):
    print(message)

talk('ごきげんよう')

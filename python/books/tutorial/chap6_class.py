#!env python3
# -*- coding: utf-8 -*-

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

class base():
    def a(self):
        print(' 私の名前は base.a です。base.b をコールします ')
        self.b()
    def b(self):
        print(' 私の名前は base.b です。der.b でオーバーライドされます ')

class der(base):
    def b(self):
        print(' ウヒョ！ オイラは der.b だよ。')

class Employee:
    pass

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

if __name__ == "__main__":
    x = MyClass()
    print(x.f())
    xf = x.f
    print(xf())

    y = Complex(3.0, -4.5)
    print(y.r, y.i)

    d = Dog('Fio')
    e = Dog('Buddy')
    print(d.kind)
    print(d.name)
    
    b=base()
    d=der()
    b.a()
    d.a()
    base.a(d)

    john = Employee()
    john.name = 'John Doe'
    john.dept = 'computer lab'
    print(john.name, john.dept)

    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")

        s = 'abc'
        it = iter(s)
        print(it)
        print(next(it))
        print(next(it))
        

        rev = Reverse('spam')
        for char in rev:
            print(char)

        for char in reverse('golf'):
            print(char)
           

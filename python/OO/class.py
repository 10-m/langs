#!env python3
# -*- coding: utf-8 -*-

class A:
    name = 'name' # class変数
    __name = 'private name' # private class value
    def __init__(self, num=0):
        self.num = num
        self.__num = 456 # private value

    def get_my_self(self):
        return self

    def show_num(self):
        num = 200
        print(self.num)
        print(num)  # 200

    def set_num(self, num):
        self.num = num
        return(self.num)

    @classmethod
    def class_method(cls, price):
        assert cls.__name__ == A.__name__
        return int(price * 0.08)

    @staticmethod
    def static_method(price):
        return int(price * 0.08)

class B(A):
    def __init__(self, num=100, str='abc'):
        super().__init__(num)
        self.str = str

    def show_all(self):
        self.show_num()
        print(self.str)



a1 = A()
a2 = A(33)

print(a1.num)
print(a2.num)
print(a1.get_my_self())
a1.show_num()
a1.set_num(123)
a1.show_num()

# class変数
print(A.name)
A.name = 'name2'
print(A.name)
print(a1.name)

# class method, static method
print(A.class_method(100))
print(A.static_method(100))

b = B()
print(b.num)
b.show_all()

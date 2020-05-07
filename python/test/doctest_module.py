#!env python3
# -*- coding: utf-8 -*-
class Keisan(object):
    def add_number_plus_double(self, num1, num2):
        '''引数同士を足して、2倍する
        >>> k = Keisan()
        >>> k.add_number_plus_double(10, 10)
        30

        '''
        # 足し算
        result = num1 + num2
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

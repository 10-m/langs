#!env python3
# -*- coding: utf-8 -*-

class PrimeIter:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        is_prime = False
        self.n += 1
        while not is_prime:
            is_prime = True
            for i in range(2, self.n):
                if self.n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                break
            self.n += 1
            if self.n >= self.max:
                raise StopIteration
        return self.n


it = PrimeIter(100)
for no in it:
    print(no, end=",")
print("")

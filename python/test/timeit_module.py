#!env python3
# -*- coding: utf-8 -*-
import timeit


def len_range(n):
    return len(range(n))

print(timeit.timeit('len(range(1000))'))
print(timeit.timeit('len_range(1000)', globals=globals()))
print(timeit.timeit('len_range(1000_000)', globals=globals()))

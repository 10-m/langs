#!env python3
# -*- coding: utf-8 -*-

import numpy as np
a = np.array([1, 2, 3])
print(a + a)

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s'\
        %(a.ndim, a.shape, a.dtype))

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print_array_details(a)

a = a.reshape([2, 4])
print(a)

a = a.reshape([2, 2, 2])
print(a)

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(x.shape)
print(x)

x = x.astype('int64')
print(x.dtype)

a = np.zeros([2,3])
print(a)

print(a.dtype)
print(np.ones([2, 3]))

empty_array = np.empty((2,3))
print(empty_array)

print(np.random.random((2,3)))

print(np.linspace(2, 10, 5)) # 2 から 10 の範囲の 5 つの数値
print(np.arange(2, 10, 2)) # 刻み幅 2 で 2 から 10 まで（10 を含まない）

a = np.array([1, 2, 3, 4, 5, 6])
print(a[2])
print(a[3:5])
print(a[:4:2])
print(a[::-1])

a = a.reshape([2,3])
print(a)
print(a * 2)
print(a - 2)
print(a / 2.0)

a = np.array([45, 65, 76, 32, 99, 22])
print(a < 50)

a = np.arange(8).reshape((2,4))
print(a)
print(a.min(axis=1))
print(a.sum(axis=0))
print(a.mean(axis=1))
print(a.std(axis=1))

pi = np.pi
a = np.array([pi, pi/2, pi/4, pi/6])
print(a)
print(np.degrees(a))
print(np.sin(a))
print(np.round(np.sin(a), 7))

a = np.arange(8).reshape((2,4))
print(a)

print(np.cumsum(a, axis=1)) # 第 2 軸に沿った累積和

print(np.cumsum(a)) # 軸引数なしで配列を平坦化する

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

a = np.arange(6)
print(a)

csum = np.cumsum(a)
print(csum)

csum[3:] = csum[3:] - csum[:-3]
print(csum)

a = np.arange(10)
print(moving_average(a, 4))


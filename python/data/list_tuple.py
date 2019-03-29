#!env python3
# -*- coding: utf-8 -*-

# concat
print((1, 2, 3) + (4, 5))

# repeat
print((1, 2, 3) * 3)

# reverse
num = [1, 2, 3, 4]
num.reverse()
print(num)

# tuple <-> list
print(tuple([1, 2, 3]))
print(list((1, 2, 3)))

# modify value with slice
nums = [1, 2, 3, 4, 5, 6, 7]
nums[0:2] = [0,0]
print(nums)

nums = [1, 2, 3, 4, 5, 6, 7]
nums[0:4] = [0]
print(nums)
nums = [1, 2, 3, 4, 5, 6, 7]
nums[0:1] = [0,0,0,0]
print(nums)

# append
nums = [1, 2, 3, 4, 5, 6, 7]
nums.append(8)
print(nums)

# insert
nums = [1, 2, 3, 4, 5, 6, 7]
nums.insert(1, 10)
print(nums)
nums = [1, 2, 3, 4, 5, 6, 7]
nums[1:1] = [13, 14]
print(nums)

# del
nums = [1, 2, 3, 4, 5, 6, 7]
del nums[1]
print(nums)
del nums[2:4]
print(nums)

# pos
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
last = nums.pop()
print(last)
print(nums)
first = nums.pop(0)
print(first)
print(nums)

# index
years = [1965, 1959, 2001, 1987, 1959, 2011]
print(years.index(1959))
try :
    print(years.index(1985))
except Exception as e:
    print(e)

# remove
years = [1965, 1959, 2001, 1987, 1959, 2011, 1959]
while True:
    try:
        years.remove(1959)
    except ValueError:
        break
print(years)

# remove duplicate
l = [1, 9, 9, 1, 3, 5]
l = list(set(l))
print(l)

# count
years = [1965, 1959, 2001, 1987, 1959, 2011]
print(years.count(1959))

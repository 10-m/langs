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

# extend
nums.extend([9,10])
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

# pop
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

# sorted
ages = [9, 15, 13, 1, 9, 77, 55, 44, 12] 
print(sorted(ages))
print(sorted(ages, reverse=True))

str1 = [{"good":3}, {"bye":2}, {"Good":1}, {"Bye":0}] 
def lower(element):
    return list(element.values())[0]

print(sorted(str1, key=lower))
print(sorted(str1, key=lambda el: list(el.values())[0]))

# sort
ages = [9, 15, 13, 1, 9, 77, 55, 44, 12] 
ages.sort()
print(ages)

# max, min
print(max(ages))
print(min(ages))
print(min(str1, key=lambda el: list(el.values())[0]))

# copy
num1 = [1,2]
num2 = num1.copy()
print(id(num1))
print(id(num2))

# clear
num2.clear()
print(num2)

# enumerate
for i, c in enumerate(['a', 'b', 'c']):
    print(i, c)

# range
for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)

for i in range(1, 5, 2):
    print(i)

# sum
print(sum([1,2,3]))
print(sum(range(101)))

# filter
heiseis = [20, 15, 4, 29, 1, 11, 10]
for s in filter(lambda h: h >= 10, heiseis):
    print(s)

# all, any
for v1 in [True, False]:
    for v2 in [True, False]:
        print('any({}, {}) = {}'.format(v1, v2, any([v1, v2])))
        print('all({}, {}) = {}'.format(v1, v2, all([v1, v2])))

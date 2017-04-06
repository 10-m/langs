for i in range(1, 4):
    print(i)

print("---")

nums = [2, 4, 6]
for i in nums:
    print(i)

print("---")

itr = iter(nums)
print(next(itr))
print(next(itr))
print(next(itr))

print("---")

def genlto3():
    print('== A')
    yield 1
    print('== B')
    yield 2
    print('== C')
    yield 3
    print('== D')

itr = genlto3()
for i in itr:
    print(i)



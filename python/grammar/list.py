a = [10, 22, 30, 45]
print(a[0])
print(len(a))
for i in a:
    print(i)

print(sum(a))

fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

b = [1, 2 ,3]
b.append(4)
print(b)

c = a + b
print(c)

b += [5, 6]
b.extend([7, 8])
print(b) # [1, 2, 3, 4, 5, 6, 7, 8]

c = [0,1,2,3,4,5,6,7,8,9]
print(c[0:2]) # [0,1]
print(c[:3]) # [0, 1, 2]
print(c[5:]) # [5, 6, 7, 8]
print(c[-1]) # 9
print(c[1:5:2]) # [1, 3]
print(c[::3]) # [0, 3, 6, 9]

del(c[2])
print(c)
del(c[1:5])
print(c)

d = [1,2,3]
x, y, z = d
print(x, y, z)

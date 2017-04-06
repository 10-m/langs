fruits = ["Apple", "Banana", "Mango", "Orange"]
print(set(fruits))

a = {1,2,3}
b = {3,4,5}
print(a - b) # {1, 2}
print(3 in b) # True
print(a | b) #{1, 2, 3, 4, 5}
print(a & b) #{3}

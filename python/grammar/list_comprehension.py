data = []
for i in range(1, 6):
    data.append(i * 2)
print(data)

data = []
data = [i * 2 for i in range(1, 6)]
print(data)

data = []
data = list(map(lambda x: x * 2, range(1, 6)))
print(data)

data = []
data = [ i for i in range(1, 6) if i % 2 == 0 ]
print(data)

result = []
base = [1, 2, 3]
for x in base:
    for y in base:
        result.append((x, y))
print(result)

result = [(x, y) for x in base for y in base ]
print(result)

result = [(x, y) for x in base for y in base if x != y]
print(result)

# set
result = {(x, y) for x in base for y in base if x != y}
print(result)

# dict
result = {"h" + str(x) : y for x in base for y in base if x != y}
print(result)

# generator
gen = (x ** 2 for x in [1, 2, 3])
for i in gen:
    print(i)

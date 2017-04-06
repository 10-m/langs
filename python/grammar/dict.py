a = { 'A' : 10, 'B' : 20, 'C' : 30}
print(a)
print(a['A'])
a['B'] *= 10
print(a)
print('C' in a) # True
print(a.keys()) #dict_keys(['C', 'A', 'B'])
print(list(a.keys())) # ['C', 'A', 'B']
print(sorted(a.keys())) # ['A', 'B', 'C']

for key in a.keys():
    print(a[key])

for key, value in a.items():
    print(key, value)
    

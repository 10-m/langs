str = 'abcdefg'
print(str.replace('abc', 'ABC')) # ABCdefg
print(str.split('c')) # ['ab', 'defg']
print(str.upper()) # ABCDEFG

str1 = "abc"
str2 = "def"
print(str1 + str2) # abcdef

print("@" * 3) # @@@

str3 = 'abcdef'
print(str3[0]) # a
print(str3[1:3]) # bc
print(str3[1:]) # bcdef
print(str3[:3]) # abc
print(str3[-1]) # f

str4 = 'a/b/c/d'
print(str4.split("/")) # ['a', 'b', 'c', 'd']
print(str4.split("/", maxsplit = 2)) # ['a', 'b', 'c/d']

a = ['aa', 'bb', 'cc']
print("-".join(a)) # aa-bb-cc

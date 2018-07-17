#!env python3
# -*- coding: utf-8 -*-

titles  =  ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
print({x:y for x, y in zip(titles, plots)})


'''
class OopsException(Exception):
    pass

a = 1
b = 0
try:
    raise(OopsException('panic'))
except OopsException as exc:
    print('Caught an oops')

''
def test(func):
    def new_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return(result)
    return(new_function)

@test
def add_inits(x, y):
    return(x + y)

add_inits(1, 2)

''
def get_odds():
    return((x for x in range(10) if (x % 2) == 1))

for number in get_odds():
    print(number)

''
def good():
    return(['Harry', 'Ron', 'Hermione'])

print(good())

''
number_thing = ('Got ' + str(number) for number in range(10))
for number in number_thing:
    print(number)

''
odds = {x for x in range(10) if x % 2 == 1}
print(odds)
''
squares = {x:x**2 for x in range(10)}
print(squares)

''
even = [x for x in range(10) if x % 2 ==0]
print(even)
''
for i in [3, 2, 1, 0]:
    print(i)

''
guess_me = 7
start = 1
while start <= guess_me:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it')
    else:
        print('oops')
        break
    start += 1

''
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

'''

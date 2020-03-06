def func(a, b):
    try:
        print(a/b)
    except:
        print("zero divied")
func(1, 2)
func(1, 0)

print('--- error class')
def func(a ,b):
    try:
        print(a/b)
    except TypeError as e:
        print("Not number: ", e)
    except ZeroDivisionError as e:
        print("Zero division: ",e)
func(1, 2)
func(1, 0)
func('a', 'b')

print('--- finally')
def func(a ,b):
    try:
        print(a/b)
    except:
        print("zero divied")
    finally:
        print("end try")
func(1, 2)
func(1, 0)

print('--- else')
def func(a ,b):
    try:
        print(a/b)
    except:
        print("zero divied")
    else:
        print("notthing error")
func(1, 2)
func(1, 0)

print('--- raise')
def func():
    try:
        raise Exception("Hello, error")
    except Exception as e:
        print(e)
func()

def for_func(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration:
            break

nums = [1, 2, 3]
for_func(nums, lambda i : print(i))

print('--- KeyboardInterrupt')
try:
    while True:
        value = input('Ctrl-C')
        print(value)
except KeyboardInterrupt:
        print('\nbye bye')


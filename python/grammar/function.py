def mul(a, b):
    ''' multipy '''
    return a * b

print(mul(10, 20))
help(mul)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

print(fact(3))

def record(name="Unknown", id=0):
    print(name, id)

record()
record("foo", 100)
record(name="bar", id=200)

def sum_args(*args):
    print(args)
    a = 0
    for n in args:
        a += n
    return a

print(sum_args(1, 2, 3))

def print_args_dict(**args):
    print(args)

print_args_dict(a=30, b=50, c=40)

def mul_func(a, b):
    return a * b

func = mul_func
print(func(4, 5))

def calc_5_3(func):
    return func(5, 3)

print(calc_5_3(func))

x2 = lambda x : x * 2
print(x2(2))

print(calc_5_3(lambda a, b: a * b))




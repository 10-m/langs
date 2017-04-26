def show_func_name(func):
    def wrapper(*args, **kwargs):
        print("--- start:" + func.__name__)
        res = func(*args, **kwargs)
        print("--- end:" + func.__name__)
        return res
    return wrapper

@show_func_name
def foo():
    print("AAA")
    print("BBB")

foo()

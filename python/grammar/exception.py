# while True:
#     try:
#         a = float(input('a? '))
#         b = float(input('b? '))
#         print(a/b)
#         break
#     except:
#         print("zero divied")

# while True:
#     try:
#         a = float(input('a? '))
#         b = float(input('b? '))
#         print(a/b)
#         break
#     except ValueError as e:
#         print("Not number: ", e)
#     except ZeroDivisionError as e:
#         print("Zero division: ",e)


# while True:
#     try:
#         a = float(input('a? '))
#         b = float(input('b? '))
#         print(a/b)
#         break
#     except:
#         print("zero divied")
#     finally:
#         print("end")

try:
    raise Exception("Hello, error")
except Exception as e:
    print(e)

def for_func(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration:
            break

nums = [1,2,3]
for_func(nums, lambda i : print(i))


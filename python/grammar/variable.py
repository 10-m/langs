a = 100
def hoge():
    global a
    a = 200
hoge()
print(a)

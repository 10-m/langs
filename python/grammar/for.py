for i in range(5):
    print(i)
else:
    print("end of for")

for i in range(5):
    print(i)
    if i == 2: break
else:
    print("end of for")

for i in range(5):
    if (i % 2) == 0 : continue
    print(str(i) + " is odd")

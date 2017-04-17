fh = open("with.tmp", mode = "w", encoding = "utf-8")
fh.write("test1\n")
fh.write("test2\n")
fh.close()

fh = open("with.tmp", mode = "a", encoding = "utf-8")
try:
    fh.write("test3\n")
    fh.write("test4\n")
finally:
    fh.close()

with open("with.tmp", mode = "a", encoding = "utf-8") as fh:
    fh.write("test5\n")
    fh.write("test6\n")

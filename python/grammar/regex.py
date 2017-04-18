import re

pattern = r"\d+"
string = "This is 100yen."
print(re.search(pattern, string))

words = [
    "oragee", "ocotorber", "octpus", "order", "banana", "baby", "busy"
]

pattern = r"oc.*"
print(pattern)
for word in words:
    if re.match(pattern, word):
        print("-", word)

pattern = r"(\d{4})/(\d{1,2})/(\d{1,2})"
string = "date: 2017/10/15"
g = re.search(pattern, string)
print(g.groups())

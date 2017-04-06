animal_list = [
    ("lion", 50),
    ("cheetah", 110),
    ("zebra", 60),
    ("reindeer", 80)
]

print(sorted(
    animal_list,
    key = lambda ani : ani[1],
    reverse = True))

animal_dict = {
    "lion" : 50,
    "cheetah" : 110,
    "zebra" : 60,
    "reindeer" : 80
}

print(sorted(
    animal_dict.items(),
    key = lambda x : x[1],
    reverse = True))

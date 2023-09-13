friends_dict = {"liem": 19, "adar": 16, "rotem": 10}
print(friends_dict)
friends_dict["joe"] = 19
print(friends_dict["joe"])
print(len(friends_dict))
print(friends_dict.keys())
friends_dict.pop("joe")
print(friends_dict)
print("jack" in friends_dict)
print("the average age is", sum(friends_dict.values()) / len(friends_dict))
for age in friends_dict.values():
    if age > 18:
        keys = list(friends_dict.keys())
        ages = list(friends_dict.values())
        print(keys[ages.index(age)])
friends_dict.clear()
print(friends_dict)

dict1 = {"name": "piyakorn", "age": "21"}
dict2 = {"name": "piyakorn", "age": "21"}
dict3 = dict1

print(dict1 is dict3)  # True

print(dict1 is dict2)  # False

print(dict1 == dict2)  # True

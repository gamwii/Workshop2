import json

# some JSON
json_string = '{"name": "Rujeongwoo", "age": 18, "city": "YG"}'


# parse x:
python_dict = json.loads(json_string)


# the result is a Python dictionary:
print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])

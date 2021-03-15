import json

# a Python object (dict):
python_dict = {"name": "RuJeongwoo", "age": 18, "city": "YG"}


# convert into JSON
json_string = json.dumps(python_dict)

# the result is a JSON string:
print(json_string)

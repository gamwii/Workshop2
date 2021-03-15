string_upper_list = []
string_list = ["jim", "por", "tide", "bb", "pang"]

for string in string_list:
    string_upper_list.append(string.upper())

print("string_upper_list", string_upper_list)





#################################
string_list = ["jim", "por", "tide", "bb", "pang"]
string_upper_list = [string.upper() for string in string_list]
print("string_upper_list", string_upper_list)

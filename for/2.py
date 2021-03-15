result = []
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    if number > 5:
        result.append(number)
print("result", result)



number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [number for number in number_list if number > 5]
print("result", result)

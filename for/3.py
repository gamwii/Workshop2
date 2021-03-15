number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mod_number = []
for number in number_list:
    if number % 2 == 0:
        mod_number.append(0)
    else:
        mod_number.append(1)
print("mod_number", mod_number)


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mod_number = [0 if number % 2 == 0 else 1 for number in number_list]
print("mod_number", mod_number)

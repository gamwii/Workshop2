num1 = 2
num2 = 1

print("--- While ---")
while num1 < 13:
    print("  [", num1, "]")
    num2 = 1
    while num2 < 13:
        print(num1, "*", num2, "=", num1 * num2)
        num2 = num2 + 1
    num1 = num1 + 1

print("\n")
print("--- For ---")
for num1 in range(13):
    if num1 == 0:
        continue
    elif num1 == 1:
        continue
    print("  [", num1, "]")
    num2 = 1
    for num2 in range(13):
        print(num1, "*", num2, "=", num1 * num2)
        num2 = num2 + 1
    num1 = num1 + 1

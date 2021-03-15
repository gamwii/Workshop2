height = int(input("Enter height : "))

i = 0
j = 0
k = 0
l = 0

while i < height:
    j = 0
    while j < height - i:
        print(" ", end="")
        j += 1

    l = 0
    j = 0
    while l <= k:
        print("*", end="")
        l += 1
    k += 2
    print()
    i += 1

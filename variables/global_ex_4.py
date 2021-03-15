x = "awesome"


def myFunc():
    global x
    print("[-] Python is " + x)  # x = aewsome
    x = "fantastic"  # เปลี่ยน x เป็น fantastic ก่อนจบ function


myFunc()
print("Python is " + x)

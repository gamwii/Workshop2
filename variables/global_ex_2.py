x = "awesome"


def myfunc():
    x = "fantastic"
    print("[-] Python is " + x) # x เป็น x ใน myfunc


myfunc()
print("Python is " + x) # x เป็น x ของ global

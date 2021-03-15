# use method pop()
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1984}
thisdict.pop("model")
print(thisdict)

# use method popitem() เอาตัวสุดท้ายออก
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1984}
thisdict.popitem()
print(thisdict)

# use del
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1984}
model = thisdict["model"]
del thisdict["model"]
print(thisdict)

# use method clear ได้ออกมาเป็น dict
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1984}
thisdict.clear()
print(thisdict)

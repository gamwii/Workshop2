# Ex 1
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = set1.union(set2)
print(set3)  # Output :{'d', 'b', 'a', 'e', 'f', 'c'}

# EX 2
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set1.update(set2)
print(set1)  # Output :{'d', 'b', 'a', 'e', 'f', 'c'}

# EX 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)  # Output :{'apple'}

# Ex 4
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)  # Output :{'google', 'cherry', 'banana', 'microsoft'}

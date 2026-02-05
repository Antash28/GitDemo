# sets are non-sequential collection of items
# cannot have indexing in sets
# sets do not allow duplicate elements
set1 = {10, "Python", 2.5}
print(set1)
print(type(set1))

# below line will give error because indexing is not allowed in sets
# print(set1[0])

print(len(set1))

# since duplicate is not allowed in sets
# therefore "1" in the below set will be printed only once
s2 = {7,9.5,11.9,23,1,73,1,4,1}
print(s2, type(s2), len(s2))

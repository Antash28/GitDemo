s1 = {2,0,-1}

# add function in set
s1.add(100)
print(s1)

# remove function in set
s1.remove(-1)
print(s1)


# if we try to add an item item in set which is already there
# we will get an error, because set does not allow duplicate elements in it
s2 = {100,200,300}
print(s2)
s1.add(200)
print(s2)

s2.discard(200)
print(s2)
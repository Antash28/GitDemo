s1 = {1,2,5,4,0,10}
s1.add(-1)
print(s1)

# frozen sets are immutable sets
s2 = frozenset({10,20,30})
print(s2, type(s2))

# below line will give error because nothing can be added to frozen set
# s2.add(-90)
# print(s2)

print(s1 & s2) #intersection
print(s1 | s2) #union
print(s1 - s2) #difference

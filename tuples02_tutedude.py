# operations on tuples
t1 = (20, 30,40,50,60,40)
t2 = (11.1, 90.89, 100.61)

# concatenation of tuple
t3 = t1+t2
print(t3)
# will be printed two times
print(t3*2)

# membership operator
# "in" and "not in"
print(100.61 in t2)
print(100.61 in t1)
print(100.61 not in t1)

# count function in tuple
print(t1.count(40))
# index function in tuple
print(t2.index(11.1))

print(max(t1))
print(min(t1))
print(sum(t1))
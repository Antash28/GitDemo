tup = (1,5,6)
print(type(tup))
print(tup)

tup1 = (1,)
print(tup1)

tup2 = (1,2,3,5,6,"red",True)
print(tup2)
print(tup2[1])
print(len(tup2))

if 3 in tup2:
    print("yes present")

if "red" in tup2:
    print("yes present")

if 0 in tup2:
    print("yes present")
else:
    print("not present")

tup5 = tup2[1:4]
print(tup5)
for i in range(5):
    print(i)

else:
    print("out of range")



# idhar else tak toh baat pohonche gee bhi nai, try it !!
for i in range(5):
    print(i)
    if i == 3:
        break

else:
    print("out of range")


# we can also use else with 'while'

i = 0
while i < 7:
    print(i)
    i = i + 1

else:
    print("out of range")

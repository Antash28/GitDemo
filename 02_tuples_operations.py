# this code will make changes in tuple by using list 
# and then convert the list back into tuple

# players = ("dhoni", "jaiswal", "bumrah", "jadeja", "raina")

# temp = list(players) # list initialized
# temp.append("Maccllum") # item added
# temp.pop(3) # item removed
# temp[2] = "brettlee" # item changed
# players = tuple(temp)
# print(players)


# new code below
# cont=("India", "UK", "US", "Netherlands", "UAE")
# cont1 = ("france", "italy", "greece", "australia")
# combined = cont + cont1
# print(combined)

# new code below
tup = (0,1,2,3,2,3,1,3,2)
res = tup.count(2)
print(res)

lap = tup.index(0)
print(lap)

cap = tup.index(3,4,8)
print(cap)

map = len(tup)
print(map)
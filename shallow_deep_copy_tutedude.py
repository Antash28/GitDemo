# shallow and deep copy concept can only be applied to the mutable data types
import copy
l1 = [1,2.5,[10,20,30],"Python"]
print(l1)

# shallow copy
l2 = copy.copy(l1)
print(l2)
print(id(l1))
print(id(l2))

l1[1] = 10
print(l1)
print(l2) #eventhough we have made changes in l1, but l2 will still remain same

l1[2][1] = 100
print(l1)
print(l2) #here we can see that l2 is also changing, we will use "deep copy"
print("\n")

l3 = [1100,201.5,[101,202,303],"CFD"]

# deep copy
l4 = copy.deepcopy(l3)
print(l4)
print(id(l3))
print(id(l4))

l3[2][1] = 0
print(l3)
print(l4) #now due to "deep copy" l4 is not changing
print("\n")

# these shallow and deep functions can be used in dictionary as well .. !!
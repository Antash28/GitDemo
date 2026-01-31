# list inside list
l1 = [5,1.5,"Python",True, None, [1,2,3], "System"]
print(len(l1))
print(l1[-6])

# we are finding the list inside l1 list and printing the element at index 2
print(l1[-2][2])

l2 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
print(len(l2))
print(l2[-1])
print(l2[-1][0])
print(type(l2))

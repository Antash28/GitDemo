t1 = ("python", 1,100,11.9,True,[1,2,3],(10,20))
print(len(t1))
print(type(t1))
print(t1[0])

# tupple can also be declared without using brackets "()" 
t2 = 3 ,5, 8, 10, 15, 20
print(type(t2))

# changing list into tupple
l1 = [10,20,30,40,50]
t3 = tuple(l1)
print(t3)
print(type(t3))

# changing tuple into list
t4 = (1,20,3,0,5)
l2 = list(t4)
print(l2)
print(type(l2))

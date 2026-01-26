s = {2,4,2,6}
# here sets will not take repeated values
print(s) 

# now here order will not be maintained, kisi bhi tarah print ho jaega "a"
a = {"Antash", 30, True, 28, 30} 
print(a)

for value in a:
    print(value)

# b = {} # this will not give <class 'set'>
       # instead this will give <class 'dict'>

b = set() # now this will give <class 'set'>
print(type(b))
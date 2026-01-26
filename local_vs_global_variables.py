x = 4
print(x) #this will print 4

def hello():
    x = 5
    print(f"The local x is {x}") #this will print 5
    print("Hello Antash")

print(f"The global x is {x}") #this will print 4
hello()
print(f"The global x is {x}") #this will print 5
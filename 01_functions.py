# function defined to calculate geometric mean
def calculateGmean(a, b): 
    mean = (a*b)//(a+b)
    print(mean)
    
# function defined to know a is smaller or bigger
def isGreater(a, b):
    if (a > b):
        print("a is bigger than b")
    else:
        print("a is smaller than b")

# taking input from user for a and b
a = float(input("enter value for a = "))
b = float(input("enter value for b = "))

# calling function
calculateGmean(a, b)
isGreater(a, b)
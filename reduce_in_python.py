from functools import reduce

numbers = [1,2,3,4,5]

# calculating sum of the numbers using "reduce" function
def mysum(x,y):
    return x+y

sum = reduce(mysum, numbers)
print(sum)
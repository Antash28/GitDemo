# def double(x):
#     return x*2

# instead of writing function as above, lambda can be used to finish in one line
double = lambda x: x*2
cube = lambda x: x*x*x
div = lambda x: x/2
avg = lambda x,y,z: (x+y+z)/3

print(double(5))
print(cube(5))
print(div(20))
print(avg(2,3,4))
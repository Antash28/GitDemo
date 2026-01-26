# FILTER

def cube(x):
    return x*x*x

# print (cube(2))

# instead of doing this
l = [1,2,4,6,4,3]
# newl = []
# for item in l:
#     newl.append(cube(item))
#     print(newl)



# we can do this, more simpler way
newl = list(map(cube,l))
print(newl)

def filter_function(a): # yeh wala function banana padega, built-in nai hota
    return a>4
newnewl = list(filter(filter_function, l))
print(newnewl)

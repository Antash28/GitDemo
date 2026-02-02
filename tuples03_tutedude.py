# mutability and immutability
# Lists are mutable
# Tuples and strings are immutable

s1 = "Python in fun"
s1.replace("Python","C++")
print(s1)

# instead we can store s1 in s2 and then print s2 to get the desired output
# after using replace function
s2 = s1.replace("Python","C++")
print(s2)

# tuples ---> it will give error since we cannot modify/change tuples
# t1 = ("mango", "banana", "apple")
# t1.append("orange")
# print(t1)

# lists
l1 = ["mango", "banana", "apple"]
# "id" ----> this give memory address
print(id(l1))
l1.append("orange")
print(l1)
print(id(l1))

# lists ---> we are trying modify/change below list using indexing
l2 = ["honda", "bmw", "ferrai"]
print(id(l2))
print(l2[-1])
l2[-1] = "ferrari"
print(l2)
print(id(l2))

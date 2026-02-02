# mutability and immutability
# Lists are mutable
# Tuples and strings are immutable

s1 = "Python in fun"
s1.replace("Python","C++")
print(s1)

# instead we can store s1 in s2 and then print s2 to get the desired output
s2 = s1.replace("Python","C++")

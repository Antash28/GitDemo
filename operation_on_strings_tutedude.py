# various operations on strings
s1 = "Python is fun\t"
print(s1[0])
print(s1[-1])
print(len(s1))

# concatenation
language = "Python\t"
version = "3.13.3"
print(language+version)

# multiplying strings
print(s1*3)

# membership operation in strings
# in
print("fun" in s1)
print("arfdfge" in s1)
print("u" in s1)

# not in
print("dfvs" not in s1)
print("is" not in s1)

# comparison of strings
print("python"=="python")

# strip ---> removes spaces 
s2 = "        Computational Fluid Dynamics      "
print(s2)
s3 = s2.strip()
print(s3)
print(s2.strip() == "Computational Fluid Dynamics")

# replace function in strings
s4 = "Antash will be a millionaire"
print(s4)
print(s4.replace("millionaire", "billionaire"))
print(s4.replace("millionaire", "MILLIONAIRE"))

# replace function in strings
s5 = "Vehicle Aerodynamics is interesting"
print(s5)
print(s5.replace("A", "a", 1)) 
# look carefully that "A" of Aerodynamics has been changed to small case "a"
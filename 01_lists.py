# marks = [3,5,6]
# print(marks)
# print(type(marks))
# print(marks[0])

# list can store different data types, example below

a = [3, 5, 6, "Antash", False, True]
print(type(a))
print(a)
print(a[3]) 

print(a[-3])
print(len(a) -3)
print(a[5-3])

if "Antash" in a:
    print("Yes")
else:
    print("No")

if "2" in a:
    print("Yes")
else:
    print("No")

if "Ant" in "Antash":
    print("Yes")

print(a[1:])
print(a[1:-1])
print(a[1:4])
print(a[1:4:2]) # this jump index
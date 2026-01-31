days = ["mon", "tues", "wed", "thur", "fri", "sat", "sun"]
print (days)

# reverse function in lists
days.reverse()
print(days)

num = [4,7,9,2,0,3,6,5]
print(num)
print("\n")
num.sort()
print("\n")
print(num)
print("\n")

# for printing in descending order
num.sort(reverse=True)
print("\n")
print(num)
print("\n")
# count function in lists
number = [9,1,3,4,7,0,5,0,2,1]
print("Options in the lists are :", number)
to_count = int(input("Enter the number to be counted : "))
print(f"the entered number is : {to_count}")
print(f"The entered number occurs : {number.count(to_count)} times in the above list")

# membership operators in lists
# in operator
lang = ["Python", "React", "C++", "C#", "Javascript"]
print("openfoam" not in lang)
print("C#" not in lang)

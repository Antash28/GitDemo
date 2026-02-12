# s1 = "Hello World"

# for char in s1:
#     print(char)

# print("The End .. !")


# # for loop with dictionaries
# employee = {"empid":1001,"name":"John Right","department":"Analysis"}

# for i in employee:
#     print(i,"=",employee[i])

# another way
employee = {"empid":1001,"name":"John Right","department":"Analysis"}

for i in employee.items():
    print(i)
    print(i[0],i[1])
    

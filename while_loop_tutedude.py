# for i in range(1,5,1):
#     print(i)
# print("***While Loop Starts below***")
# # above code can be written using while loop

# num = 1
# while num<5:
#     print(num)
#     num = num+1

# another example
correct_password = "CFD"
while True:
    user_password = input("Enter the passsword : ")
    if user_password == correct_password:
        print("Password Accepted")
        break
    else:
        print("Not Accepted")
        
print("You are logged in")
print("----Password Check Completed Here----")

# another example
x=10
while x<=20:
    print(x)
    x=x+2

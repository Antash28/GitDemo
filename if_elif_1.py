num = int(input("enter the value of num = "))

if(num<0):
    print("Number is negative")
elif(num==0):
    print("number is zero")
elif(num==999):
    print("Special number is entered")
else:
    print("number is positive")
    
# this will always be printed because indentation is wrong  
print("******")
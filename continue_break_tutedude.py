for num in range(10):
    if num%3==0:
        continue
    print(num)
print("---end---")

# using break 

for num in range(1,10):
    if num%3==0:
        break #the moment when "if condition" is "true" the "break statment" will terminate the loop and will go out of line 13
    print(num)
print("---end---")

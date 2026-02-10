num = int(input("Enter a number : "))

if num%2==0:
    print("even number")
else:
    print("odd number")

# above "if else" can be written in "one line"
print("EVEN") if num%2==0 else print("ODD")

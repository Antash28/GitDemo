try:
    num = int(input("Enter an integer : "))
    a = [6 , 3]
    print(a[num])

except ValueError:
    print("This is not an integer")

except IndexError:
    print("Index Error")

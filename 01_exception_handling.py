a = input("enter the number : ")
print("multiplication table of {a} is : ")

try:
    for i in range(1, 11):
        print(f"{int(a)} * {i} = {int(a) * i}")

# except Exception as e:
#     print(e)

# or this way
except:
    print("Invalid Entry ! ")

print("some important lines of code")
print("End of Program")
def welcome():
    print("Hello, how are you ?")

print(__name__) #this will give "__main__" as an output, meaning it is executing from first.py itself

if __name__ == "__main__":

    welcome()
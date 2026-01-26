def func():

    try:
        l = [1,5,6,7]
        i = int(input("enter the index : "))
        print(l[i])
        return 1
    except:
        print("error occured")
        return 0
    
    # this will execute everytime with any input given by the user
    finally:
        print("I am always executed")

# lets again try this way as in previous code "01_finally_keyword.py"
# is code mein yeh print nai chalega
    # print("I am always executed")

x = func()
print(x)

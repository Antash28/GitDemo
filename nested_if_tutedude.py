marks = float(input("Enter marks : "))

if marks>=60:
    print("passed")
    if marks>=90:
        print("grade A")
    elif 80<=marks<90:
        print("grade B")
    elif 70<=marks<80:
        print("grade C")
    else:
        print("grade D")
else:
    print("best luck next time")
    
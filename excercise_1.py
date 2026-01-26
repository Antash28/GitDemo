# this program is capable of greeting the user with good morning
# this program is capable of greeting the user with good afternoon
# this program is capable of greeting the user with good evening

time = float(input("Enter the time in 24 hour format (ex:1:00PM = 13) = "))

if (time <= 12):
    print("Good Morning")

elif (time > 12):

    if (time > 12 and time <= 16):
        print("Good Afternoon")

    elif(time > 16 and time <= 21):
        print("Good Evening")

    else:
        print("Good Night")

else:
    print("invalid entry")


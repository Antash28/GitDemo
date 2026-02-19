#write a program to simulate a dice (for example in ludo)
import random

print("Welcome to the dice game .. !")

while True:
    choice = input("Press 'Enter' to roll a dice or 'q' to quit the game.")
    if choice == "q":
        print("Not playing")
        break
    elif choice == "P":
        number = random.randint(1,6)
        print(f"your number is {number}")
    else:
        print("Invalid Input")
print("out of game")


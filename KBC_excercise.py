# taking user's name as an input
name = input("Hello, enter your good name : ")
print("\nHello,",name.capitalize(),",good day !")

# taking age as an input from the user
age = float(input("\nEnter your age to check if you are eligible to play KBC: "))

# function to check user's age
def ageCheck(age):   
    if age >= 18:
        print("\nAge Verified, you are eligible to play\n")
        print("Enjoy the game :)\n")
        return True
       
    else:
        print("\nYou should be atleast 18 to play the game\n")
        print("Exiting the session, thank you\n")
        exit()

# calling function    
ageCheck(age)

# taking 1 as input from the user to start the game
startGame = float(input("\nPress 1 to start the game: "))

# function to start with the game and display first question
def game(startGame):   
    if startGame == 1:
        print("\nFirst question right on your screen\n")
        return True
    
    else:
        exit()

# calling function  
game(startGame)

MoneyEarned = 0

# question number 1
Q1 ="Under whose captaincy, did Indian Men's Cricket Team, won all the 3 major ICC Trophies ?\n"
print("Q1 : ", Q1)

Opt1 = ["A) Sachin", "B) Ganguly", "C) Dhoni", "D) Rohit"]
print("\nOptions: ", Opt1)
print("\n(correct answer will give you 1000 rupees)\n")

ans = input("Enter your answer : ")
print("\nThe answer entered is : ", ans,"\n")

if ans == "C) Dhoni":
    print("correct answer!\n")
    MoneyEarned = 1000
    print("Congratulations, you have earned Rs = ", MoneyEarned,"\n")
    print("lets move on to the second question\n")

else:
    print("wrong answer!\n")
    print("Well played, you will take home Rs = ", MoneyEarned,"\n")
    exit()

# question number 2
Q2 ="Which team has never won IPL in last 18 years ?"
print("Q2 : ", Q2)

Opt2 = ["A) SRH", "B) RCB", "C) CSK", "D) KKR"]
print("\nOptions: ", Opt2)
print("\n(correct answer will give you 2000 rupees)\n")

ans = input("Enter your answer : ")
print("\nThe answer entered is : ", ans,"\n")

if ans == "B) RCB":
    print("correct answer!\n")
    MoneyEarned = MoneyEarned+1000
    print("Congratulations, you have earned Rs = ", MoneyEarned,"\n")
    print("lets move on to the third question\n")

else:
    print("wrong answer!\n")
    print("Well played, you will take home Rs = ", MoneyEarned,"\n")
    exit()

# question number 3
Q3 ="What is the mass of 1 litre of water ?"
print("Q3 : ", Q3)

Opt3 = ["A) 1", "B) 2", "C) 3", "D) 5"]
print("\nOptions: ", Opt3)
print("\n(correct answer will give you 3000 rupees)\n")

ans = input("Enter your answer : ")
print("\nThe answer entered is : ", ans,"\n")

if ans == "A) 1":
    print("correct answer!\n")
    MoneyEarned = MoneyEarned+1000
    print("Congratulations, you have earned Rs = ", MoneyEarned,"in total\n")

else:
    print("wrong answer!\n")
    print("Well played, you will take home Rs = ", MoneyEarned,"\n")
    exit()
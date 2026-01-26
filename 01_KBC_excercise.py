Question = [
    
[
    
    "Q1) Under whose captaincy, did Indian Men's Cricket Team, won all the 3 major ICC Trophies ?\n", 
            "Sachin", "Ganguly", "Dhoni", "Rohit", 2
],

[
    "Q2) Which team has never won IPL in last 18 years ?\n", "SRH", "RCB", "CSK", "KKR", 1
],

[
    "Q3) What is the mass of 1 litre of water (in kilograms) ?\n", "1", "2", "3", "5", 0
],
]
    
levels = [1000, 2000, 3000]

for i in range (0, len(Question)):
    ques = Question[i]
    print(ques[0])
    print(f"(Question for Rs {levels[i]})\n")
    print(f"A) {ques[1]} B) {ques[2]}")
    print(f"C) {ques[3]} D) {ques[4]}\n")

    reply = int(input("\nEnter your answer (1-4) (1 for Sachin, 2 for Ganguly ans so on ) :"))

    if(reply == ques[-1]):
        print(f"\ncorrect answer, you have won Rs {levels[i]}\n")

    else:
        print("wrong answer")
        exit

# print(f"your take home money is Rs {levels[i]}")
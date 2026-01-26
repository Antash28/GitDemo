applePrice = int(input("Enter the price of apple in per kg: "))
budget = int(input("Enter your budget: "))

if(budget - applePrice > 50):
    print("Alexa, add 1 kg apples in the cart")
elif(budget - applePrice > 70):
    print("Alexa, you can still add 1 kg apples in the cart")
else:
    print("out of budget")
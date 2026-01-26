applePrice = int(input("Enter the price of apple in per kg: "))
budget = int(input("Enter your budget: "))

if(applePrice<=budget):
    print("Alexa, add 1 kg apples in the cart")

else:
    print("out of budget")
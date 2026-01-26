import first

#first.welcome()

# even if you comment "first.welcome()", 
# Hello, how are you ? --> this will get printed, coming from "first.py"
# but this is a serious problem, but why ??
# kyuki "first" module import karte he uske andar jo bhi hai woh execute ho raha hai
# this should not happen, import karte he execute nai hona chaiye, file delete bhi so sakti hain
# now to prevent this go back to "first.py" to check  __name__ == __main__
# now when this is used in "first.py" --> __name__ == __main__
# then just buy importing "first" will not execute anything, we will need to call the welcome func
# but it will execute if you go to "first.py" and run it which is perfectly fine !
def greet(fx):
    def mfx(): # this is modified function(fx) ---> "mfx"
        print("good morning")
        fx() 
        print("thanks for using this function")
    return mfx


@greet # this is a decorator (decorator ek function ko modify kar deta hai)
def hello():
    print("Hello world")

hello()
greet(hello)() # aise bhi likh sakte hain, alternatively "@greet"
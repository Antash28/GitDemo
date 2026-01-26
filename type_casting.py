a="1"
b="2"
print(a+b)

# ab isko samjhte hain ki 3 kaise aega aur 12 na aae

# now this is called type-casting which will give 3 instead of 12
print(int(a)+int(b)) 

# another example

string="15"
number=7

# throws an error if the string is not a valid integer
string_number = int(string)   
sum=number+string_number
print("the sum of both the number is:", sum)

# now lets understand implicit type-casting
c=1.9
d=8
print(c+d)
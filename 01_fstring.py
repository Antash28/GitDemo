letter = "Hello my name is {} and I am from {}"
country = "India"
name = "Antash"

print(letter.format(name,country))

# now if we make the above print line opposite
print(letter.format(country,name)) # we will get placement error for "Antash" and "India"



# soultion for this placement issue
# we place 0 and 1 in the letter
letter1 = "Hello my name is {1} and I am from {0}"
country1 = "India"
name1 = "Antash"
print(letter1.format(country1,name1))



# but 0 and 1 makes things more complex 
# what now ??
# we will use "fstring"
print(f"Hello my name is {name} and I am from {country}") # "fstring" is used here


# another example
price = 100
txt = f"for only {price:.2f} rupees."
print(txt)
# range is a built in function used to generate sequence of integers in a given interval
# for i in range(start,stop,step) #this is a range syntax

for i in range(1,11,2):
    print(i)
print("---end---")
# another example
# reverse order
for x in range(20,9,-1):
    print(x)
print("---end---")

# another fun example
for y in range(10,-1,-1):
    print(y)
print("Happy New Year 2026")

# another example with range function
# here step is by-default 1
for z in range(1,6):
    print(z)
print("---end---")

# another example with range function
for a in range(6):
    print(a)

# another example
groceries = ["salt","milk","jaggery"]
for item in groceries:
    print(item)

for index in range(len(groceries)):
    print(index)

# another example
profits = [9,11,6,10]

for index in range(len(profits)):
    quarter = index+1
    print(f"Profit for quarter {quarter} is {profits[index]}")

    
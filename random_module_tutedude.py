import random

# print(random.random())
# print(random.randint(1,100))

x = [12,34,56,101,0,47]
y = ["apple","grapes","banana","papaya"]
print(random.choice(x))
print(random.choice(y))
random.shuffle(y)
print(y)

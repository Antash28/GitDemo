# lists are declared by using square brackets []
student1 = ["Antash", 32, 95.5]
print(type(student1))
print(student1)

# example 2
days_of_the_week = ["Mon","Tues","Wed","Thur","Fri", "Sat","Sun"]
print(days_of_the_week[0])
print(days_of_the_week[2])
print(days_of_the_week[4])
print(days_of_the_week[6])
print(f"last day of the week is {days_of_the_week[6]}")
print(f"last day of the week is {days_of_the_week[-1]}") 

# length of the "list" is number of elements/items in the "list"
print(len(days_of_the_week))

# below line will throw an error because above list does not have 8th element/item
print(days_of_the_week[8])

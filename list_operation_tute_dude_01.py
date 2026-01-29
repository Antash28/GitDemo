# slicing of lists
l1 = [3,8,1,0,4,9,7,3,6]
print(len(l1))
print(type(l1))

# slicing below
print(l1[1:6:1])

# concatenation of lists
l2 = [1,2,3,4,5]
l3 = [6,7,8,9,10]
# elements of list l2 will be printed first and then l3
print(l2+l3)
# elements of list l3 will be printed first and then l2
print(l3+l2)

print(l2*3)

# append function
# adds an item in the end of the list
fruits = ["mango", "apple", "orange"]
print(fruits)
fruits.append("banana")

# below line will show "None" because here append func is not returning anything
print(fruits.append("banana"))
# there fore we have to separately print "fruits"
# so that "banana" can be added in the list as the last item
print(fruits)

# insert function
# with this function we can decide where the element should be placed in the list
# unlike "append" which adds an element/item in the end
food = ["Rice", "Panner", "Rajma","Choley"]
print(food)
food.insert(2,"Salad")
print(food)



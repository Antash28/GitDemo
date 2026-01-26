marks = [12, 56, 32, 98, 41, 45, 1, 4]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("raajey ! ")
#     index = index + 1


# now we will use enumerate function to wrote the above code    
index = 0
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("raajey ! ")
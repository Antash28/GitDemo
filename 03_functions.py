# def average(*numbers):
#     # taking it as tuple, tuple not yet studied
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("the avg is : ", sum / len(numbers))

# average(1, 2)


# another way to write the above code :-
def average(*numbers):
    # taking it as tuple, tuple not yet studied
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

c = average(1, 2)
print(c)

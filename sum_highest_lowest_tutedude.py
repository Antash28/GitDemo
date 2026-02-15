# 1st method to calculate the total score 

scores = [2,14,250,46,97,36,7,100,110,0,1]
# print(len(scores))
# sum = 0
# for i in range(len(scores)):
#     sum = sum+scores[i]
# print(f"{sum} is the total score for team A")


# 2nd method to calculate the total score 
# total = 0
# for score in scores:
#     total = total+score
# print(f"{total} is the total score for team A")


# 3rd method to calculate the total score 
# total = sum(scores)
# print(f"{total} is the total score for team A")

# getting highest score
highest = scores[0] #assumption that the first value is the highest
for score in scores:
    if highest < score:
        highest = score
# highest = max(scores) #just this line can also be used to get the highest value
print(highest)         

# getting highest score
lowest = scores[0] #assumption that the first value is the highest
for score in scores:
    if lowest > score:
        lowest = score
# lowest = min(scores) #just this line can also be used to get the highest value
print(lowest)

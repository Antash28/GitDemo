stud1 = {"english","maths","chemistry", "physics","CS"}
stud2 = {"english","biology","chemistry", "physics"}
stud3 = {"sanskrit","maths","CS"}

print(stud1, type(stud1))
print(stud2, type(stud2))

# common subjects of stud1 and stud2
# either we can write "intersection" or use symbol "&"
# common_sub = stud1.intersection(stud2)
common_sub = stud1 & stud2
print(common_sub)

# union subjects of stud1, stud2 and stud3
# either we can write "union" or use symbol "|"
# union_sub = stud1.union(stud2, stud3)
union_sub = stud1 | stud2 | stud3
print(union_sub)


# another example
day = {"mon","tues","wed","thur","fri","sat","sun"}
weekends = {"sat","sun"}

common_day = day & weekends
print(common_day)

all_day = day | weekends 
print(all_day)

# printing below the difference between the sets
weekdays = day.difference(weekends) # another way to calculate the ddiference
# weekdays = day - weekends 
print(weekdays)

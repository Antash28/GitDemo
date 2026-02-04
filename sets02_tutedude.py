nums = {1,3,2,0,-1}

# membership operator ----> in / not in
print(0 in nums)
print(3 in nums)
print(9 in nums)
print(9 not in nums)
print(2 not in nums)

# concatenation in sets
s2 = {34,21,90,76}
# below line will give error because concatenation with "+" operator is
# not allowed in sets
# print(nums+s2)

# below line will give error because repetition with "*" operator is
# not allowed in sets
# print(nums*2)

days = ("mon","tues","wed","thur","fri","sat","sun")
days = set(days)
print(days)


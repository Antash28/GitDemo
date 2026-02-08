# more operations in dictionary
# d1 = {[1,3,5]:9,[1,2,1]:4}
# print(d1) #this will give error, because we have used "lists" in the "dict"

# below we have used list inside dict
student1 = {"id":1001,"name":"John","marks":[80,70,10]}
print(student1)
print(student1["marks"])
print(student1["marks"][1])

# below we have used dict inside dict

student2 = {"id":1005,"name":"Max","marks":{"eng":80,"maths":70,"phy":10}}
print(student2["marks"])
print(student2["marks"]["phy"])
print('\n')

# only fetching the "keys"
print(student1.keys())
print(student2.keys())
print('\n')
# only fetching the "values"
print(student1.values())
print(student2.values())
print('\n')
# only fetching the "items"
print(student1.items())
print(student2.items())
print('\n')
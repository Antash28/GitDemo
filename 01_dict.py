dic = {"Antash": "Successful Man",
       "CFD": "Computational Fluid Dynamics"
       }

print(dic["Antash"])

dic_1 = {28:"Antash Sinha",
         5: "M.K.Sinha",
         7:"M.S.Dhoni"}

print(dic_1[28])

info = {'name':'Antash', 'age': 28, 'eligible': True}
print(info)

# print(info["name"])
# print(info.get('name'))

# # print(info["name1"]) # this will thro error since 'name1' is not there in 'info'
# print(info.get('name1')) # but this will print 'none'

print(info.keys())
print(info.values())

for key in info.keys():
    # print(info[key])
    print(f"The value corresponding to the key {key} is {info[key]}")
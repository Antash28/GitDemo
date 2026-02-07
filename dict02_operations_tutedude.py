marks = {"maths":80,"eng":70,"physics":95}
print(marks)
print(marks["eng"])

#get() function in dictionaries
print(marks.get("eng"))

emp1 = {"id":1001,"name":"System","salary":10000000}
print(emp1.get("phone")) #this give output as none since "phone" is not present
                        # in the "dict" above

print(emp1.get("phone", 897582)) #here 897582 get printed instead of "None"

# membership operator in dict
# "in"
print(1001 in emp1) #this gives "false" as output because 1001 is present as "value"
print("id" in emp1) #this gives "true" because this given as "key" in the above dict

emp1["phone"] = 9435032
print(emp1) #here "phone" will be added in the dictionary

# more examples on dict operations
sem1 = {"maths":80,"phy":100,"Python":95}
sem2 = {"chem":66,"english":70}
print(sem1,sem2)

sem1.update(sem2)
print(sem1)

sem1.pop("phy")
print(sem1)

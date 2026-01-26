# class person:
#     name = "Antash"
#     occu = "Aerodynamics Engineer"

#     def info(self):
#         print(f"{self.name} is a {self.occu}")

# a = person()
# print(a.name)
# a.name = "Max"
# a.occu = "Developer"

# a.info()




# another way to write the above code using "__init__"
class person: ## yaha pe "person" naam ki class banadi
    def __init__(self, n, o):
        print("Just for testing !!")
        self.name = n
        self.occu = o

    def info(self):
        print(f"{self.name} is a {self.occu}")

## here "a" is for "self", "Antash" is for "n" and "Aerodynamics Engineer" is for "o"

a = person("Antash", "Aerodynamics Engineer") # here "a" is a object
b = person("Max", "Developer") # here "b" is a object
a.info()
b.info()
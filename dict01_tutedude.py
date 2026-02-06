# dictionaries are comma separated key-value pairs enclosed within "{}"

groc = {'milk':58,'cake':10,'rice':90,'rajma':100}
print(groc)
print(type(groc))
print(len(groc))
# print(groc[0]) #this line will gice error, because indexing is not allowed
               # in dictionaries
print(groc['rice'])

# dict are mutable
groc['rice'] = 50 #here the price is updated for "rice"
print(groc)

# print(groc['eggs']) #this line gives error, because eggs is not yet added
                    # in the dictionary "groc"

groc['eggs'] = 5 #here "eggs" will be added to the dict "groc"
print(groc)


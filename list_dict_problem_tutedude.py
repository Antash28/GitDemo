# we have a dictionary containing details
# we need to delete the sensitive information from the dictionary such as password, address

user = {"Username": "Han","Password" : "123", "Email Id" : "xyz@gmail.com", "Address" : "522, NS Road","Country":"India"}
sensitive_information = ["Address","Password"]

for i in sensitive_information: 
        user.pop(i)
        
print(user)      

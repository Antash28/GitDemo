countries = ["India", "Germany", "Australia", "United Kingdom", "Russia", "Netherlands", "Ireland"]

counter = 0
output = []
for country in countries:
    if country.startswith("I"):
        counter = counter+1
        output.append(country)
print(f" total no of countries starting with letter I is {counter} and their names are {output}")
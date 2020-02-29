print("5. Find the age of the youngest person")
ages = {'Peter': 52, 'Hannah': 19, 'Simone': 32, 'myself': 28}

# to get only the age:
# dictname.values() method
agesval = ages.values()
ageslist = list(agesval) # returns list of all the values which are numbers

youngster = ageslist[0] # youngest may be defined by index 0 of list 
for age in ageslist:
    if age < youngster:
        youngster = age

print(youngster, 'is the age of the youngest person in the dict')

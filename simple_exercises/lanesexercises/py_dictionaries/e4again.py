print("4. Find the name of the youngest person")
ages = {'Peter': 52, 'Hannah': 19, 'Simone': 32, 'myself': 28}

# alkey = ages.keys() # works both ways:
# print(list(alkey))    # name_of_dict.keys() returns object 'dict_keys'
ali = list(ages.keys()) # list(dict_keys) returns the list of it

# loop through ali to find youngest
youngest = 80000  #humanly impossible
pers = '' 
for pers in ali:
    if ages[pers] < youngest:
        youngest = ages[pers]
        name = pers
print(name, 'is ', youngest, 'years old, and the youngest person in the dictionary. ')
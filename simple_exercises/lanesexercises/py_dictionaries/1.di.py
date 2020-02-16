#     Python-dictionaries

# 1. Create an empty dictionary
ages={}

# 2. Use the dictionary to store the age of persons, and add three persons to the dictionary (with their age), including yourself

ages["Peter"]=52
ages['Simone']=32
ages['ich']=27
ages['Hannah']=18

# 3. Find your age in the dictionary  --> for all values print(ages.values())
print(ages['ich'])

# 4. Find the name of the youngest person
print('exercize 4')
youngest = ages['Peter'] #starts at first entry youngest carries value of the key peter.
for el in ages:
    if ages[el] < youngest:
     youngest = ages[el] # youngest assumes value of current key.
# each time el assumes the next key - which is the name of the person.
print("The name of the younges person is ", el)

# 5. Find the age of the youngest person
youngest = ages['Peter'] #starts at first entry youngest carries value of the key peter.
for el in ages:
    if ages[el] < youngest:
     youngest = ages[el] # youngest assumes value of current key.
print(youngest)

# 6. Remove yourself from the dictionary
print('removing myself')
del(ages['ich'])

# 7. Compute the average age
sum_ages=0
lenght= len(ages)
for key in ages:
    sum_ages += ages[key]
print(sum_ages/lenght)
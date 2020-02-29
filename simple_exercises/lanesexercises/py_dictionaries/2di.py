#  Python-dictionaries

# 1. Create an empty dictionary
firstdict = {}
# 2. Use the dictionary to store the age of persons, and add three persons to the dictionary (with their age), including yourself
firstdict['Peter'] = 52 ; firstdict['Hannah'] = 19 ; firstdict['Simone'] = 32
firstdict['myself'] = 28

print(firstdict)

# 3. Find your age in the dictionary
# for i in firstdict:
#     if firstdict[i] == 28:
#         print('I found my age in the dictionary')
#probably better or more correct:
myage = firstdict['myself']
print(myage)

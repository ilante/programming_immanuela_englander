# 3. define a function called “add3” that returns the sum of three numbers
# 4. define a function called “add5” that returns the sum of five numbers
#jumped 3. and 4. its the same as previous

# 5. define a function that takes as input a number and a string and returns as many copies of the string as specified by the number. I.e. manyTimes(3,’dad’) should return ‘daddaddad’
def manytimes(num, stri):
    for i in range(num):
        print(stri)
    
manytimes(4, "AnA")
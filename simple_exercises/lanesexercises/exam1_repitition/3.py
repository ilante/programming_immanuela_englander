# Write a function that takes a string and returns true if the string only contains 'A' and 'T', false otherwise.

# AT
# ATG
def only_a_an_t(str):
    for letter in str:
        if letter != "a" and "t": #union is or 
            return False
        else:
            return True

str1 = "ta"
print(only_a_an_t(str1))
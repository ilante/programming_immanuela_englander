# Exercise 1
x = "Fire and ice"

#Exercise 2
print(x[3])

#Exercise 3
print(x[5])

#Exercise 4
print(x[10])
print(x[-1])
print(x[-2])

#Exercise 5: prints characters in even positions in a string
print(x[::2])

#Exercise 6: prints the characters in odd number positions in a string
print(x[1::2])

#Exercise 7: Prints the first half of a string
print(x[:len(x)//2])

#Exercise 8: This exercise takes a string and prints it upside down
print(x[::-1])

#Exercise 9: counts the number of e's and i's in a string
e = x.count("e")
i = x.count("i")
print("There are", e, "e's and", i, "i's in the string")

#Exercise 10
x = x.replace("and","&")
print(x)

#Exercise 11, 12 & 13: searches for a string or character in another string
print("re &" in x) # This option displays "true" is the character is in the string or false if it is not
print(x.count("re &")) #This option displays the number of times the string or character is found in the template string
print(x.find("re &")) #This option displays the position of the first character when found in the string, or -1 when not found

#Exercise 14 & 15: this algorithnm finds the first and the last e positions in the string
char="e"
x1 = x.find(char)
x = x[::-1]
x2 = len(x)-x.find(char)-1
w = [x1,x2]
print(w)      

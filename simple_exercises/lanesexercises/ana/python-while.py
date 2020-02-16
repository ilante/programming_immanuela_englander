#Exercise 1: slide 9 of the while lesson.
done = "done"
char = None
while char != done:
    char = input(">>")
    print (char)
print ("bye!")

#Exercise 3: this code prints all the characters in a string and prints them until it finds two consecutive equal characters (should not be printed)
char1 = "Ana"
i=0
out = ""
while i < (len(char1)-1) and char1[i] != char1[i+1]:
        out += char1[i]
        i+=1
        if i == len(char1): 
            out += char1[-1]
print (out)


#Exercise 4: this code asks the user for a number and prints the numbers until there is an even number, then prints the number of tries.
i=1
while True:
    number = input("insert a number:")
    if (int(number) % 2) != 0:
        print (int(number))
    else:
        break
    i+=1
print ("The number of tries is:",i)

#Exercise extra: this function to check weater any of the following patterns occur in a given string.
import re
def searchpat(seq):
    match = re.search(r"[GAC]C[GC]",seq)
    if match:
        return (True)
    else:
        return (False)
print(searchpat("AAGGGTCCGTGCGAGGTA"))




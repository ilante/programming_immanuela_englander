# 1) Function that takes a string as a paratmeter and returns true if str contains at least 3 g false otherwise.

def gizz(stringa):
    gsum = 0
    for letter in stringa:
        if letter == 'g':
            gsum += 1
    if gsum >= 3:
        return True
    else:
        return False

# 2) funciton that takes a list of integers and returns the max of the 2 last elements
inli = [1,2,5,100, 58]
# print(inli[-2:-1])
# print(inli[-1:-2:-1])

def limax(inli):
    secondlast = inli[-2]
    last = inli[-1]
    if secondlast > last:
        return secondlast
    else:
        return last
    

print(limax(inli))

# 3) A function that takes a file handler as a parameter 
# and returns the number of characters in the 
# first line (you can assume that the file exists and contains at least 2 lines).
#  
# Write a program that invokes the function on a file whose name is taken from the user.

# def thefunction(infile):
#     line1 = infile.readline()
#     # print(line1)
#     return len(line1)

# #ask the user for the file
# filename = input('please type in the absolute file path')
# userfile = open(filename, 'r')
# print(thefunction(userfile))

# 4) A function that takes strings from the user until the user insterts the string 'Hello' the program then prints on the screen the number of inserted strings and the strings.
def talktome():
    talk = ''
    talksum = []
    while talk != 'Hello':
        talk = input("Write something ")
        talksum.append(talk)
    sum = len(talksum)
    return sum, talksum

print(talktome())

# labs/PY0101EN/PY0101EN-4-1-ReadFile.ipynb
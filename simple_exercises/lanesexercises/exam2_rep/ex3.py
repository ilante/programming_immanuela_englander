# 3) A function that takes a file handler as a parameter and returns the number of characters in the first line (you can assume that the file exists and contains at least 2 lines). Write a program that invokes it on a file whose name is taken from the user

def handler(filehandler):
    firstLine = filehandler.readline().rstrip()
    Num_char = len(firstLine)
    return Num_char

file_name = input("Please enter the file name plus extension. ")
infile = open("./" + file_name, "r")

# invoking handler on a file
x = handler(infile)
print(x)

# line1 = infile.readline()
# print(line1)
# 3) A function that takes a file handler as a parameter and returns the number of characters in the first line (you can assume that the file exists and contains at least 2 lines). Write a program that invokes it on a file whose name is taken from the user

file_name = input("file name:")
file_name = "./"+file_name +", ' r'"
infile = open(file_name)
# print(file_name)
#You need an extra step here in order to add the "./filename.txt" for it can be taken as an argument in the following function
x=file_name.readline()
print(x)


# 4) A function that takes strings from the user until the user insterts the string 'Hello' the program then prints on the screen the number of inserted strings and the strings.
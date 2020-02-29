# # assign the number 3 to a variable called tre
# tre = 3

# # assign the string "3" to a variable called three

# three = '3'

# # convert the variable tre to string and concatenate three and tre, assign the resulting string to a new variable
# tre = str(tre)
# dd = tre+three

# define a function that takes a list of numbers as parameter and returns the sum of the list
li = [1,2,3,4,5]
def sumli(lista):
    sum = 0
    for el in lista:
        sum += el
    return sum

# # open the file numbers and read the first line. Print that line.
# with open('./numbers', 'r') as infile:
#     one = infile.readline()
#     print(one)

# # create a function that takes as its only parameter a file name. 
# # The function must open the file, read the first line and return it. 
# # Use the function to get the firs line of the file numbers and print it
# def op_read_1stLine(filename):
#     with open('./'+filename, 'r') as infile:
#         firstline = infile.readline()
#         return firstline

# x = op_read_1stLine("numbers") # need to add '' to the string of the filename
# print(x)

# # write a function that takes a filename as parameter, 
# # opens that file reads the first line, 
# # converts the line into a list of numbers and then uses the pevious function to calculate the sum of the numbers. 
# # return the sum


# write a function that takes a filename as parameter, 
# opens that file reads the first line, converts the line into a list of numbers and returns it
def sum_firstline(filename):
    with open('./'+filename, 'r') as filobject:
        sum = 0
        li = []
        string_line = filobject.readline()
        strnums = string_line.split()
        return strnums

n = 'numbers'
print(sum_firstline(n)) #file name needs '' ""

# write a function that takes a filename as parameter, 
# opens that file reads the first line, 
# converts the line into a list of numbers 
# then uses the pevious function to calculate the sum of the numbers. 
# return the sum

def fi_sum(filename):
    with open(filename, 'r') as ofile:
        strinum = ofile.readline().split() # .split() returns list
        num = []
        sum = 0
        for stri in strinum:            # ['12', '3', '43', '456', '6', '57', '6', '68', '79']
            num.append(int(stri))
        sum = sumli(num) 
    #     for number in num:
    #         sum += number
    return sum

num = fi_sum('numbers') #the file name needs to be "i
print(num)



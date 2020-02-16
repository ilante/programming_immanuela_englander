#Exercise 1: This code takes two lists and joins them together
a=[4,8,-9,"the"]
b=["silent force",4.67,9]
c= a+b
print(c)

#Exercise 2: This code extracts each character in a list
my_list = [23,64,354,-123]
for i in my_list:
    print(i)


#Exercise 3: This code performs a summatory of each of the elements in a list.
def addlist(x):
    a=0
    for i in x :
        a = a+i
    return(a)
y=[1,2,3,4,5]
print(addlist(y))

#Exercise 4: This code takes the number from list in exercise 2, and uses the function "addlist" from point 3 to add them up 
my_list = [23,64,354,-123]
def addlist(x):
    a=0
    for i in x :
        a = a+i
    return(a)
y=my_list
print(addlist(y))

#Exercise 5: this algorithnm takes a list as an input, and displays its partial summatory as a list.
def partial_sum(y):
    sum=[]
    n=0
    for i in y:
        n = n + i
        sum.append(n)
    return(sum)
c = [1,2,3,4,5,6,7,8,9]
suma = partial_sum(c)
print(suma)

#Exercise 6: two functions that create and display an n*n matrix of #'s
#This function creates a matrix consisting of n elements with n elements each
def square_matrix(n):
    matrix = [] #Creates an empty list
    for i in range(n): #For each element in a series that goes from 1 to n
        row = []       #create a new list, which will be the rows of the matrix
        for x in range(n): #for each element in a series that goes from 1 to n 
            row.append("#") #Add a "#" simbol to the row
        matrix.append(row)  #To the empty matrix add each of the rows that were already created by the previous for loop
    return(matrix)          #return the matrix (note the matrix will be a list of n elements consisting of n elements each one -- in this case a list of 3 elements consisting of 3 elements each)
matrix = square_matrix(10)   #execute the function and assign it to the value matrix


#This function displays the matrix in a matrix form
def impr_matrix(matrix):    
    var = ""   #set an empty string where the values will be stored
    for y in range(len(matrix)):  #For each element in the range of the lenght of the core matrix
        for p in matrix[y]:      #for each element in the y position of the matrix (first cycle: would execute matrix[0], second: matrix [1], third: matrix[2] and so on)
            var += str(p) + "\t" #assign each element of the position of the matrix to a string called var, using a space between them
        var += "\n"               #After the prior cycle has been executed, print the var variable adding a "jump" between them
    return(var)

#Exercise 7: print the multiplication table
def mult_table(num):
    table = [] #Creates an empty list
    for i in range(1,num+1): #For each element in a series that goes from 1 to num + 1 (because multiplication table starts in 1 and not in 0)
        row = []       #create a new list, which will be the rows of the table
        for x in range(1,num+1): #for each element in a series that goes from 1 to num +1
            row.append(x*i) #Add the number of x multiplied by i (e.g the first row (x = 1-10) will all be multiplied by the first i = 1, the second row (x = 1-10 again) will be multiplied by i = 2 and so on)
        table.append(row)  #To the empty table add each of the rows that were already created by the previous for loop
    return(table)          #return the table (note this will be a list of "num" elements consisting of "num" elements each one.
table = mult_table(11)   #execute the function and assign it to the value table
print(impr_matrix(table))

#This shows an alternative for the multiplication table
for i in range (1,11):
    st= ""
    for j in range (1,11):
        st= st + " " + " " * (3-len(str(i*j))) + str (i*j)
    print (st)

#Exercise 1: This function takes any given number and returns the value of the number + 1
def increase(y): 
    return(y+1)

#Exercise 2: This function takes two numbers and adds them up
def add(x,y):
    return(x+y)

#Exercise 3: This function takes 3 numbers and adds them up 
def add3(x,y,z):
    return(add(x,y) +z)

#Exercise 4: This function takes 5 numbers and adds them up
def add5(x,y,z,a,b):
    return (add3(x,y,z)+a+b)

#Exercise 5, 6 & 7: This function takes a string and multiplies it "num" number of times separated by the specified "sep" separator
def timesastring (num,string,sep):
    """num= number of times to repeat a string; string=word or string to be repeated; sep=separator"""
    return(num*(string+sep))[:-1]
y= timesastring(4,"dad",",")
print(y)
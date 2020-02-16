#Exercise 1
x = 2.24
print(x)

#Exercise 2
y = 3.14

#Exercise 3: takes a number and displays if the number is even or odd
even = x%2 #This operator is used to find the "residue" of a number divided by another number. 
if even != 0:
    print(x, "is an odd number")
else:
    print(x, "is an even number")

#Exercise 4: find the average of two numbers.
Avrg = (x+y)/2
print("The average of", x, "and", y, "is", Avrg)

#Exercise 5
x = x*2 - 1
print(x)

#Exercise 6 & 7: this algorithm takes the coordinates of two different points in space and returns the euclidean distance between them
from math import sqrt
x1 = 1
x2 = 2
y1 = 3
y2 = 4
distance = sqrt((x2-x1)* (x2-x1) + (y2-y1)*(y2-y1))
print ("The Euclidean distance between the two points is:", distance)

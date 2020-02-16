# Write a function that takes a list of integers and returns the sum of the elements smaller than 7.

def elsm7(li):
    sum=0
    for el in li:
        if el < 7:
            sum += el
    return sum

intlist = [1,2,3,4,5,6,7,8,9,10,11]
print(elsm7(intlist))
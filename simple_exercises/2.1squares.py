# 2 Looping functions
# Define the following functions in Python, usually by using a for loop.
# 2.1 Squares
# Given a list of numbers l, evaluate their squares: resulti = li2 ∀i ∈ l
l=[1,2,3,4,5,6,]

def squares(list):
    for el in list:
        print(el**2)

squares(l)
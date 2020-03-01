
# 4. Using functions from points 1. and 3., 
# define a function that takes an integer and returns its square if it is even, the number itself otherwise

def squrs(num):
    sqrnum = num**2
    return sqrnum

def even(num):
    if num%2 == 0:
        return True
    else:
        return False

def even_sq_odd_itself(num):
    if even(num) == True:
        return squrs(num)
    else:
        return num

print(even_sq_odd_itself(2))
print(even_sq_odd_itself(-5))

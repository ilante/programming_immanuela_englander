# 4. Using functions from points 1. and 3., define a function that takes an integer and returns its square if it is even, the number itself otherwise
# def squares(a):
#     squared = a*a
#     return squared

# print(squares(10))

# def even(a):
#     if a%2 == 0:
#         return True
#     else:
#         return False

def even_sq_odd_number(inte):
    squared = inte*inte
    if inte%2 == 0:
        return squared
    else:
        return inte
print(even_sq_odd_number(100))
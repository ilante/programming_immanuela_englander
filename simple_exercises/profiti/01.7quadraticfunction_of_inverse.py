#Given three coefficients a, b, c and a value x, evaluate the function
def qufuofinverse(a, b, c, x):
    fx= a*1/(x*x) + b/x + c
    return fx

y= qufuofinverse(1, 3, 4, 5)
print(y)
# 1.12 Cases
# Given a number a, evaluate its square if it is odd, otherwise divide it by 2 􏰔a2 if x is odd
# f(a) = a otherwise 2
def squ_or_odd(a):
    if a%2!=0:
        return a*a
    else:
        return a/2

x=squ_or_odd(9)
print(x)
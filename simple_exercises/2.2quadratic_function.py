# 2.2 Quadratic function
# Given three coefficiels a, b, c and a list L, evaluate the quadratic function for every value of L.
# Hint: exploit the function defined in 1.6
#qu funciton
def quadrfct(a, b, c, list):
    for el in list:
        fx = a*(el*el)+b*el+c
        return fx

l=[1,2,3,4,5,6,]
y=quadrfct(1, 2, 2, l)
print(y)
#factorial Given a number n evaluate its factorial n!
def factorial(n):
    product=0
    for i in range(n):
        factor = i+1
        product=factor*factor
    print(product)
factorial(3)
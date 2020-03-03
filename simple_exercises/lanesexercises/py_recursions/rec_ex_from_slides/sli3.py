#factorial: n * (n-1)

# trying the 'normal way'
def factori(n):
    res = n
    while n != 1:
        res = res * (n-1)
        n -= 1
    return res

print(factori(5))

# trying recursion from slide

def factorial(n):
    result = 1
    for k in range(1, n+1): # n+1 because last num in range not incl
        print(k)
    #     result = result * k
    # return result

print('the other')
print(factorial(5))

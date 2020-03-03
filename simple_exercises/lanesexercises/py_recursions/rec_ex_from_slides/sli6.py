''' Math inductive definition: 
a) 0 != 1                  
b) n! = n * [ (n-1)! ]

python functional recursive function:
a) if n == 0:
     return 1
b) else:
     return n * n factorial(n-1)    '''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(3))

# is recursion magic ----> YES !!! so its use is not allowed in the vatican
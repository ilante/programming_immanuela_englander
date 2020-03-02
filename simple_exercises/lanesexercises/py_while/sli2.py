# while; while the condition is true the loop continues
# once the condition is false: the while ends
# if the cond is initially false: the body is never executed
# The body should contain commands that change the value of variables used in the while condition
#otherwise we get INFINITE LOOPS

def sequence(n):
    while n != 1:
        print(n)
        if n%2 == 0:    #n is even
            n = n//2
        else:           # ne is odd
            n = n*3+1

print(sequence(8))

#the program will be stuck in an infinite loop if n = 0

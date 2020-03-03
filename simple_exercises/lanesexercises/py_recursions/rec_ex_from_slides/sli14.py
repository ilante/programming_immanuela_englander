def powe(base, exp):
    if exp == 0:
        return 1
    else:
        return base ** exp

print(powe(10, 2))

# now recursive:

def pow(base, exp):
    if exp == 0:
        return 1
    else:
        return base * pow(base, exp - 1)

print(pow(10, 3))

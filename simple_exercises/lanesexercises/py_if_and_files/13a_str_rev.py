# a13. print both strings in reverse
a = 'anna'
h = 'Gruber'

c = a+h
print(c[::-1])

# 14. evaluate which one of the two strings is palindrome (i.e. a string is palindrome if it can be read in the same way both from left to right and from right to left)
def palindro(s1, s2):
    if s1 == s1[::-1]:
        print(s1 + ' is a Palindrome')
    else:
            print(s1, ' is not a Palindrome')
    if s2 == s2[::-1]:                
        print(s2 + ' is a Palindrome')
    else:
        print(s2, ' is not a Palindrome')

palindro(a, h)


# 15. print the first half of the first string and the second half of the second one
a = 'anna'
g = 'Gruber'
halfstring_a = a[:len(a)//2]
halfstring_g = g[len(g)//2:] #from middle index to end
halv_a_g = halfstring_a+halfstring_g
print(halv_a_g)
print(g[len(g)//2:])

# n= "nana"
# print(n[:3])
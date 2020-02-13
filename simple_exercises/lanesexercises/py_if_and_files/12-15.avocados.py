# 12. put the string “avocado” in a variable and the string “radar” in another one
a='avocado'
r='radar'
# 13. print both strings in reverse
print(a[::-1])
print(r[::-1])
# 14. evaluate whether any of the two strings is palindrome (i.e. a string is palindrome if it can be read in the same way both from left to right and from right to left)
def palindrome(str):
    if str == str[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")

palindrome(a)
palindrome(r)

# 15. print the first half of the first string and the second half of the second one
print('first half of each string')
def halfstring(stri):
    print(stri[:len(stri)//2])

halfstring(a)
halfstring(r)
# 4) A program that takes strings from the user until the user insterts the string 'Hello' the program then prints on the screen the number of inserted strings and the strings.
i=0
while True:
    user = input("Please write strings ")
    if user == "Hello!":
        i += 1
        print(i)
        break 
    else:
        i += 1
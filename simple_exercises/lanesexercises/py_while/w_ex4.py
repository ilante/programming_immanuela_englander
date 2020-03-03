# 4. Ask numbers to the users until it inserts an even number. Print the number of tries.
tries = 0
num = 1
while num%2 != 0:
    num = int(input('gimme a number. '))
    tries += 1
else:
    print("you tried ", tries, 'times.')
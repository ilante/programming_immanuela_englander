# 1. create a list of numbers from 3 to 12
# 2. print the numbers of the list that are odd
li=[1,2,3,4,5,6,7,8,9,10,11,12]
for num in li:
    if num%2 != 0:
        print(num)

print(" ")
print("example 5")
print(" ")
# 3. print the numbers of the list that are multiples of 5
for el in li:
    if el%5 == 0:
        print(el)

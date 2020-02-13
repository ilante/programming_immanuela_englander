# 4. put the values 5,2,7,8,1,-3 in a list, in this order
li=[5,2,7,8,1,-3]
# 5. print the first and the third value in the list
print('question 5')

print(li[0], li[2])

# 6. print the double of all the values in the list
print('question 6:')
doubleli=[]
for el in li:
    dob = el*2
    doubleli.append(dob)
print(doubleli)

# 7. print each value in the list after doubling it, subtracting 2 and dividing by 3
print('question 7:')
dobsubs2div3=[]
for num in li:
    newnum = (num*2/3)-2
    dobsubs2div3.append(newnum)
print(dobsubs2div3)

# 8. print the sum of all the numbers in the list
print('sum of all the numbers in the list')
sumli=0
for num in li:
    sumli += num
print(sumli)

# 9. print the minimum value in the list
print('The minimum value is:')
li=[5,2,7,8,1,-3]
min=li[0]
for el in li:
    if el < min:
        min = el
print(min)
# 10. print the maximum value in the list
max=li[0]
for el in li:
    if el > max:
        max=el
print(max)
# 11. print the average value
sum=0
for el in li:
    sum += el
print(sum/len(li))
# 4. put the values 5,2,7,8,1,-3 in a list, in this order
li = [5,2,7,8,1,-3]
# 5. print the first and the third value in the list
li[2]
# 6. print the double of all the values in the list
for num in li:
    dobli=num+num
    print(dobli)
    
# 7. print each value in the list after doubling it, subtracting 2 and dividing by 3
for num in li:
    dob_minus2_div3=((num+num)-2)/3
    print(dob_minus2_div3)
# 8. print the sum of all the numbers in the list
sum=0
for num in li:
    sum +=num

print(sum)

# 9. print the minimum value in the list
min = li[0] # i cant start at number 0 so i start at index 0
for num in li: # iterate through each number
    if num < min: # if current number of list is smaller than the first
        min = num # call that one the min (or assign it to the min)

print(min)

# 10. print the maximum value in the list
max = li[0]
for num in li:
    if num > max:
        max = num

print(max)
# 11. print the average value
sum_all = 0
for i in li:
    sum_all += i 

print(sum_all/len(li))

li = [5,2,7,8,1,-3]
# # 1. Create a list of numbers from 3 to 12
# linum = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# # 2. print the numbers of the list that are odd
# oddli=[]
# for e in linum:
#     if e%2 == 0:
#         oddli.append(e)
# # odd = linum[::2]
# print(oddli)
# # 3. print the numbers of the list that are multiples of 5
# print(5%5)
# fivers=[]
# for el in linum:
#     # print(el)
#     if el%5==0:
#         fivers.append(el)
# print(fivers)
# 4. change the list so it contains the numbers from 8 to 23
linum = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(linum)

longlist = []
for el in linum:
    if el >= 8:#:P
        longlist.append(el)
    
print(longlist)

for number in longlist:
    for i in range(11):
        i=12
        longlist.append(i+1)

print(longlist)


    
# newlist = []
# for el in linum:
#     print(el)
#     if el > 8:
#         newlist.append(el)

# print(newlist)

#     if el >= 12:
#         linum.append(el+1)
# print(linum)
# n=12
# for el in range(11):
#     n=n+1
#     linum.append(n)
# print(linum)
# # 5. repeat steps from 9 to 10 for the new list
# # for pos in linum[9:10]:
# #     print(pos)

# #     Idont know what to do
# #############################################
# #############################################
# # 6. put the values 5,2,7,8,1,-3 in a list, in this order
# newli = [5,2,7,8,1,-3]
# # 7. print the first and the third value in the list
# print(newli[0], newli[3])
# # 8. print the double of all the values in the list
# doubli = []
# for number in newli:
#     doubli.append(number*2)

# print(doubli)
# # 9. print each value in the list after doubling it, subtracting 2 and dividing by 3
# crazylist = []
# for newnumber in newli:
#     crazylist.append((newnumber*2)-(3/2))

# print(crazylist)
# # 10. print the sum of all the numbers in the list
# sum = 0
# for e in crazylist:
#     sum = sum + e

# print(sum)
# # 11. print the minimum value in the list
# # for i in crazylist

# 12. print the maximum value in the list
# 13. print the average value

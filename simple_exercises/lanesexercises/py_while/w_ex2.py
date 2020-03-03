# 2. Use a while loop to compute the partial sums of a list of integers

li = [1, 2, 3, 4, 5]

# now with a while:
i = 0 
partsum = 0
while i != len(li):
    partsum += li[i]
    i += 1
    print(partsum)

# tried with for as well

part_sum = 0
lasti = len(li)
for i in range(lasti):
    part_sum += li[i]
    print(part_sum, 'round', i)
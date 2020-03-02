#     Python-while

# 1. Use a while loop to compute the sum of a list of integers

testli = [-1, 1, 1, -1]

sum = 0 
lungo = len(testli)
i = 0 

while i != lungo: # because last index is smaller than lungo
    sum += testli[i]
    i += 1
print(sum)

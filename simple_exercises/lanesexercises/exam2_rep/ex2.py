
# 2) funciton that takes a list of integers and returns the max of the 2 last elements

def last_two(li):
    max = 0
    last = li[-1]
    secondlast = li[-2]
    if last > secondlast:
        max = last
    else:
        max = secondlast
    return max

lis = [1,2, 1, 4]

maxi = last_two(lis)
print(maxi)
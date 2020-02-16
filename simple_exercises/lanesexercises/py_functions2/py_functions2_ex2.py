# 2. Use the function to compute the square of all numbers of a given list
def squares(a):
    squared = a*a
    return squared

li = [1, 2, 3, 4, 5]
lisq=[]

for el in li:
    sq = squares(el)
    lisq.append(sq)

print(lisq)
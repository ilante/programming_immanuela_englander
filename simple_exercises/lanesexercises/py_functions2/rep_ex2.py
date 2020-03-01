# 2. Use the function to compute the square of all numbers of a given list
def squrs(num):
    sqrnum = num**2
    return sqrnum

li = [17, 2500, 1, -5, 0, 3]
sq_li = []
for i in li:
    sqares = squrs(i)
    sq_li.append(sqares)

print(sq_li)

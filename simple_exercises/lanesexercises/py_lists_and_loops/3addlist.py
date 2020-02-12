# 3. define a function called “addlist” that returns the sum of the elements of any list
def addlist(Liste):
    sum=0
    for el in Liste:
        sum+=el
    return sum

lila=[100, 1, 20]
print(addlist(lila))
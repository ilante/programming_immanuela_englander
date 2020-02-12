# 4. use the function addlist from point 3 to sum the numbers from point 2
x='23|64|354|-123'
y=x.split("|")
print(y)
number_list =[] # need to append int transformed stringnum
for i in y:
    number_list.append(int(i))
print(number_list)

def addlist(Liste):
    sum=0
    for el in Liste:
        sum += el
    return sum

print(addlist(number_list))
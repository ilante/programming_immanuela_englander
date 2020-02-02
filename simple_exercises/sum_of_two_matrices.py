A=[[1,2, 8], [3, 7,4]]
B=[[5,6, 9], [7,6 ,0]]
c=[]
for i in range(len(A)): #range of len gives me indecesc.
    c.append([])
    for j in range(len(A[i])):
        sum = A[i][j]+B[i][j]
        c[i].append(sum)
print(c)
# for i in range(len(A)): #range of len gives me indeces
#     for j in range(len(A[i])): #again indeces
        # sum = A[i][j]+B[i][j]
    #     rowlist.append(sum)
    # print(rowlist)
    # rowlist =[]


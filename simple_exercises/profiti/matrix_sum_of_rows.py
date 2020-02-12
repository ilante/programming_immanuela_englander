# L=[['a', 'b', 'c','d'], ['z', 'y', 'x', 'w']]
# for i in L:
#     print(i)

# for i in range(len(L[0])):
#     print(i)
M=[[1,1,1],[2,2,2], [3,3,3]]
lista=[]
suM=0
# print(len(M[0]))
# print(M[0][1])
for i in range(len(M)):
    for e in M[i]:
        # print(e)
        suM=suM+e
        
print(suM)
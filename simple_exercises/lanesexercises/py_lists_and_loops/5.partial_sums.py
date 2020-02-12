
# # 5. write a function that takes a list of integers and computes the list of its partial sums
li=[1,2,3,4,5,5,5,4, -4]

def partsumlist(li):
    r=len(li[2:])
    partial_sum=0
    partial_sum += li[0] + li[1] #starting by adding index 1 and 2
    part_sum_list=[]
    for i in range(r):
            partial_sum += li[i+2]
            part_sum_list.append(partial_sum)
    return part_sum_list
#    print(part_sum_list)

y=partsumlist(li)
print(y)
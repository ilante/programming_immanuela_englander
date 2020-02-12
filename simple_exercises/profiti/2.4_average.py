# 2.4 Average
# Given a list of numbers l, evaluate their average
l=[1, 2, 3, 5]

def average_li(li):
    index=0
    sum_el=0
    for element in l:
        index = index+1
    num_of_el=index
    print("the list has", num_of_el, "elements")
    for element in l:
        sum_el += element
    print(sum_el/num_of_el)

average_li(l)
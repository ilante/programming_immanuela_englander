# sum(of_list) is built in

def mysumli(li):
    if li == []:
        return 0
    else:
        return li[0] + mysumli(li[1:])


# print(li[0:-4])
lis = [1, 1, 1]
print(mysumli(lis))
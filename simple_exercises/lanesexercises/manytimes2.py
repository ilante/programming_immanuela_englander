# 6. modify the previous function so that it returns something like ‘dad,dad,dad’
def manytimes(num, stri):
    joined = (stri + ",")*num
    print(joined[:-1])
    
manytimes(4, "AnA")
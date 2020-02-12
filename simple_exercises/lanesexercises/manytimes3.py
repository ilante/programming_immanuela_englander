
# 7. modify the function at point 5 so you can specify a separator instead of just using the comma like in point 6
def manytimes(num, stri, sep):
    joined = (stri + sep)*num
    print(joined[:-1])
    
manytimes(4, "AnA", ",")
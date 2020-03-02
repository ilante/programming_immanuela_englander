# https://www.codesdope.com/practice/python-while/
# Print the following patterns using loop :
# c.
# 1010101
#  10101 
#   101  
#    1   

st = '1010101'
space = " "
i = 0
stl =len(st)
# print(st[0:stl])
while i != 5:
    print(st)
    st = space+st[i+2:len(st)]
    space = i*space
    i += 1

# 1010101
#   10101 
#    101  
#     1   

# 1010101
#   10101 
#     101
#       1
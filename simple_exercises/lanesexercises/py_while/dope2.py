# https://www.codesdope.com/practice/python-while/
#  Print the following patterns using loop :
# b.
#    *  
#  *** 
# *****
#  *** 
#    *  

i = 0
st = ''
while i < 4:
    st += '*'
    i += 1
    print(st)
while i > - 1:
    st = st[0:i]
    i -= 1
    print(st)
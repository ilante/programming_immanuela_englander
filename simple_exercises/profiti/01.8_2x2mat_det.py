#1.8 2x2 matrix determinant

def twox2mat_det(l):
    det =l[0][0]*l[1][1] - l[0][1]*l[1][0]
    return det

l=[ [1, 2], [3, 4]]
y=twox2mat_det(l)
print(y)
def mat(row, col):
    biglist=[]
    for j in range(row):
        row = []
        for j in range(col):
            row.append('x')
        biglist.append(row)
    return biglist
    
mat(4,5)
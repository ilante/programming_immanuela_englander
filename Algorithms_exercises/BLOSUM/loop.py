seq1='ATGC'
seq2='AGC'
gap_penalty = -2
matrix=[]

for row in range(len(seq2)+1):
    sublist = []
    if row == 0:
        for column in range(len(seq1)+1):
            sublist.append(gap_penalty * column)
        matrix.append(sublist)
# print(matrix)
    else: 
        for column in range(len(seq1)+1): #generates list of lenght of Horizontal seq1
            if column == 0:
                sublist.append(gap_penalty * row)
            else:
                sublist.append(0)
        matrix.append(sublist)

print(matrix)
    
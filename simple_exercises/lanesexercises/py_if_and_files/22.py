# 18. print 3 rows: the first and the third for the sequences, the second one should contain “|” if
# the bases are complementary, “X” if not. Example:
# ATTCGT
# ||X|X|
# TAGGAA

# 22. Modify the program from point 18 in order to print also the number of non complementary positions (in the given example: 2)
di_seq ={"A":"T", "T":"A", "G":"C", "C":"G"}

se1 = 'ATTCGTTT'
se2 = 'TAGGAACC'

print(se1)
pattern = ""
countX=0
for i in range(len(se1)):
    if se1[i] == di_seq[se2[i]]:
        pattern += "|"
    else:
        pattern += "X"
        countX += 1
print(pattern)
print(se2)
print("The number of mismatches is", countX)

# 23. Modify the previous programs in order to read the sequences from file, using them in pairs (i.e. first row with second row, third with fourth and so on) Note: each pair of strings must have the same length (i.e. first and second row must have the same length, for example 6, third and fourth row may have both length 9 etc)
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



# 24. Modify the previous programs in order to read the sequences from file, checking for each one with all the others of the same length for the one with the smallest number of non complementary positions. Print each string with its best match and score as in point 22.
# Example:
# Input file
# ATTCGT
# TAGGAA
# TCAGCA
# AAAAAAAAA
# TTTTTTTTT
# Result:
# ATTCGT and TCAGCA with 1 non complementary position
# TAGGAA and ATTCGT with 2 non complementary positions
# TCAGCA and ATTCGT with 1 non complementary position
# AAAAAAAAA and TTTTTTTTT
# TTTTTTTTT and AAAAAAAAA
# 25. Modify the previous programs so to write the results in a new file

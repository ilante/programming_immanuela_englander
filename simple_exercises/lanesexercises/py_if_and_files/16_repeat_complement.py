# 16. ask the user for two strings
one = input('Give me one word please! ')
two = input('Give me another one. ')

# 17. check if one string is the complement of the other (i.e. “AC” and “TG” -> yes)
bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def complement(seq1, seq2, di):
    pattern = ''
    for i in range(len(seq1)):
        if seq1[i] == bases[seq2[i]]:
            pattern += '|'
        else:
            pattern += 'X'
    print(seq1)
    print(pattern)
    print(seq2)

complement(one, two, bases)

# 18. print 3 rows: the first and the third for the sequences, the second one should contain “|” if
# the bases are complementary, “X” if not. Example:
# ATTCGT
# ||X|X|
# TAGGAA
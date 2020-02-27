# 23. Modify the previous programs in order to read the sequences from file, using them in pairs (i.e. first row with second row, third with fourth and so on)

# 24. Modify the previous programs in order to read the sequences from file, checking for 
# each one with all the others 
# of the same length 
# for the one with the smallest number of non complementary positions. 
# Print each string with its best match and score as in point 22.
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

bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def complement(seq1, seq2, di):
    if len(seq1) != len(seq2):
        print('sequences not equal in length')
        return
    number_misma = 0
    pattern = ''
    for i in range(len(seq1)): # to get the index we need the range of len seq1. Range starts at zero by default and doenst include last number
        if seq1[i] == bases[seq2[i]]: # acess bases with key of seq2 in index i 
            pattern += '|'
        else:
            pattern += 'X'
            number_misma += 1
    print(seq1)
    print(pattern)
    print(seq2)
    print('There are ', number_misma , 'mismatches')

with open('./23.seq.txt', 'r') as infile:
    lines = infile.readlines() #reads all the lines and returns list of all lines
    print('The file has ', len(lines), 'lines.')
    for i in range(1, len(lines), 2): #starts at line one prints every other line 1, 3, 5
        one = lines[i-1].rstrip()
        two = lines[i].rstrip()
        # one = one.rstrip()
        # two = two.rstrip()
        complement(one, two, bases)
        print('')
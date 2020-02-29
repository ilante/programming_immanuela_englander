# 24. Modify the previous programs in order to read the sequences from file, 
# checking for each one with all the others 
# of the same length for the one with the 

# smallest number of non complementary positions. 

# Print each string with its MATCH and score as in point 22.

bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def complement(seq1, seq2, di):
    if len(seq1) != len(seq2):
        return -1, '' # if 2 stings of unequal len we return -1 and empty string to be consistent in the values returned
    pattern = ''
    noncompl = 0
    compl = 0
    for i in range(len(seq1)):           # to get the index we need the range of len seq1. 
                                         # Range starts at zero by default and doenst include last number
        if seq1[i] == bases[seq2[i]]:    # acess bases with key of seq2 in index i 
            pattern += '|'
            compl += 1
        else:
            pattern += 'X'
            noncompl += 1
    # if compl > 0:
    #         print(seq1, ' and ', seq2, 'have ', compl, ' complimentary pairs in the alignment.')
    # elif noncompl > 0:
    #         print(seq1, ' and ', seq2, 'have ', noncompl, ' mismatches in the alignment.')
    # print(seq1)
    # print(pattern)
    # print(seq2)
    # print('number of noncomplimentary positions is', noncompl)
    return noncompl, pattern # only the value of noncompl is returned NOT the variable_name (its lost)

# noncompl = complement('ATC', 'TAG', bases) #small test

with open('./23.seq.txt', 'r') as infile:
    lines = infile.readlines() # makes list 'lines' [ contains all lines] \n in the end of each string except last line
    print('The file has ', len(lines), 'lines.')
    # counter = 0 to check if it runs through all
    for i in range(len(lines)): # creates variable that holdes index for elements of 'lines'=[...]
                                # starts at line 0 ends at len - 1  = the last line. becaus last number is never includet   like in [1:9] 9 is not included.
        min_noncompl = 100000000 
        min1 = ''
        min2 = ''
        minpattern = ''
        for j in range(len(lines)): # j holds also index for elements of 'lines'=[...] - so each i can be compared with     each j
            if lines[i] == lines[j]: #so if you encounter the same sequence (line) move to next j - so no comparisson with self.
                continue    # means go up to for j in range... and go to next j
            else:
                one = lines[i]
                two = lines[j]
                one = one.rstrip()
                two = two.rstrip()
                noncompl, pattern = complement(one, two, bases) #calling the function and dfining variable for noncompl which is returned by the function
                if noncompl == -1: #to skip when strings are of different lenght see line 13
                    continue
                if pattern == '':
                    continue
                if noncompl < min_noncompl:
                    min_noncompl = noncompl
                    minpattern = pattern
                    min1 = one
                    min2 = two
        if min_noncompl != 100000000:
            print("The smallest number of non complementary positions is ", min_noncompl )
                        # " the pattern is: ", "\n", minpattern)
            print(min1)
            print(minpattern)
            print(min2)
        else:
            continue

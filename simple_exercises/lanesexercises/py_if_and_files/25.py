# 24. Modify the previous programs in order to read the sequences from file, 
# checking for each one with all the others 
# of the same length for the one with the 
# smallest number of non complementary positions. 
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

# 25. Modify the previous programs so to write the results in a new file

bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def complement(seq1, seq2, di):
    if len(seq1) != len(seq2):
        # print('') # empty line for unequal lenght
        # print("seq 1 i ", seq1, 'and seq 2 j', seq2, ' are not equal in length')
        return
    pattern = ''
    noncompl = 0
    for i in range(len(seq1)): # to get the index we need the range of len seq1. Range starts at zero by default and doenst include last number
        if seq1[i] == bases[seq2[i]]: # acess bases with key of seq2 in index i 
            pattern += '|'
        else:
            pattern += 'X'
            noncompl += 1
    # if noncompl > 0:
    #     print(seq1, ' and ', seq2, 'have ', noncompl, ' noncomplimentary positions.')
    # else:
    #     print(seq1, ' and ', seq2, ' are a PERFECT match.')
    
    # print('number of noncomplimentary positions is', noncompl)
    return noncompl # only the value of noncompl is returned NOT the variable_name (its lost)

# noncompl = complement('ATC', 'TAT', bases) small test

with open('./23.seq.txt', 'r') as infile:
    lines = infile.readlines() #because of /n character in the end
    print('The file has ', len(lines), 'lines.')
    counter = 0

    for i in range(len(lines)): #starts at line one prints every other line 1, 3, 5
        lowest_mismatch = 8000000000000 #keeps lowest of each set =, so only counts lowest of on j round.
        lowest_one = ''
        lowest_two = ''
        for j in range(len(lines)):
            if lines[i] == lines[j]: #so if you encounter the same line move to next j
                continue
            else:
                one = lines[i]
                two = lines[j]
                one = one.rstrip()
                two = two.rstrip()
                noncompl = complement(one, two, bases) # complement() returns none if strings are empty, 
                # calling the function and dfining variable for noncompl which is returned by the function
                counter += 1
                if noncompl == None:
                    noncompl = 8000000000000
                    continue
                if noncompl < lowest_mismatch:
                    lowest_mismatch = noncompl
                    lowest_one = one
                    lowest_two = two
                
                # round = 'round ' + counter+' '
        if lowest_mismatch == 8000000000000:
            continue
        
        print(lowest_mismatch, lowest_one, lowest_two)  
        # if i > 0:
        #     print(" index of i means ", i+1, ' loops finished ')
        # if i == 0: 
        #     print(' index', i, ' is the first ROUND of an entire j loop ')
        # if i+1 == 10:
        #     print(' The', i+1 , 'lines of the file have been compared each one to each')


    # with open("./25.py", "a") as outfile:

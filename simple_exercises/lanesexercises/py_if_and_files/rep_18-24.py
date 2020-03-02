# 18. print 3 rows: the first and the third for the sequences, the second one should contain “|” if
# the bases are complementary, “X” if not. Example:
# ATTCGT
# ||X|X|
# TAGGAA

# 22. Modify the program from point 18 in order to print also the number of non complementary positions (in the given example: 2)

# 23. Modify the previous programs in order to read the sequences from file, using them in pairs (i.e. first row with second row, third with fourth and so on) Note: each pair of strings must have the same length (i.e. first and second row must have the same length, for example 6, third and fourth row may have both length 9 etc)
# 24. Modify the previous programs in order to read the sequences from file, checking for each one with all the others of the same length for the one with the smallest number of non complementary positions. 
# 
# Print each string with its best match and score as in point 22.

bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def seqcheck(s1, s2):
    pattern = ''
    num_of_complementary_positions = 0  
    for i in range(len(s1)):
        if s1[i] == bases[s2[i]]:
            pattern += '|'
            num_of_complementary_positions += 1
        else:
            pattern += 'X'
    return s1, pattern, s2, num_of_complementary_positions

def seqcheck_fromfile(fileName):
    with open(filename, 'r') as infile:
        line_list = []          #why do i not need readline()???
        for line in infile:
            line_list.append(line.rstrip())

        count = 0
        for i in range(len(line_list)):
           
            max_score = 0
            best_1 = ''
            best_pattern = ''
            best_2 = ''

            for j in range(len(line_list)):
                if i != j:
                    if len(line_list[i]) == len(line_list[j]):
                        s1, pattern, s2, score = seqcheck(line_list[i], line_list[j])
                        count += 1
                        if score > max_score:
                            max_score = score
                            best_1 = s1
                            best_pattern = pattern
                            best_2 = s2
                    else:
                        continue
                else:
                    continue
            print("The best alignment is")
            print(best_1)
            print(best_pattern)
            print(best_2)
            print('with a score of ', max_score, "\n")
        print(count)

filename = './seq.txt'
seqcheck_fromfile(filename)

# Print each string with its best match and score as in point 22.
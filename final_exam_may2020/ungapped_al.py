# final version
def score_aln(s1, s2, scoring_dict):
    '''Takes two sequences and a scoring dictionary as input, and returnes
    the the alignment score of 2 sequences of the same lenght'''
    tot_score = 0                   # initiate score at 0 
    for i in range(len(s1)):        # counts
        pair = s1[i] + s2[i]        # pair concattenation of s1 and s2 at corresponding index
        if "-" not in pair:         # if true (no dash in pair), so there is no gap in the alignment
            tot_score += scoring_dict[pair] # increment total score by value from scoring dict
    return tot_score

def ungapped_best_aln (s1, s2, scoring_dict): 
    '''Takes as input 2 sequences (can be of different length) and a scoring dictionary. Returns an ungapped
    alignment and its score.'''                                        # 1 2 3 4 5
                                                                       # - - T C A         
    aln_len = len(s1) + len(s2)         # sum length of the alignment  G A - - - 
    fill_gaps1 = list("-" * len(s2))    # generating as many gaps as necessary - always as long as the other sequence
    fill_gaps2 = list("-" * len(s1))
    aln = [fill_gaps1 + list(s1), list(s2) + fill_gaps2] # --- are added to beginning of s1 BUT appended to s2
    best_score = -1                    # initializing score at -1                                                                           
    for i in range(aln_len):  
        seq_string1 = "".join(aln[0])  # extracts element 0 from list and transforms it into a string
        seq_string2 = "".join(aln[1])  # extracts element 1 from list and transforms it into a string
        
        score = score_aln(seq_string1, seq_string2, scoring_dict) # calling function

        if score > best_score:          # only if score is larger than the best_score,
           
            best_score = score          # best_score takes value of 'score' if lager than 'best_score'
            best_pair = ["".join(aln[0]), "".join(aln[1])] # assignes the best scoring alignment to 'best_pair'
     
#             print(aln) [['-', '-', 'T', 'G', 'A'], ['G', 'A', '-', '-', '-']]

            
        if aln[1][-1] == "-":            # if last pos in s1 is a gap
            aln[1] = aln[1][-1:] + aln[1][:-1] # moves last element in front
        else:                            # in case last el is NOT a gap
            aln[0] = aln[0][1:] + aln[0][:1]  # first element is moved to the back
        # print(str(aln[0]))        #print to see if they slide as they should.
        # print(aln[1])
        # print('Score', best_score)
    return best_pair, best_score


print(ungapped_best_aln("TGA", 'GA', blosum50))
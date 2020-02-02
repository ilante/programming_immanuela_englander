# 18.Ask user ofr two strings,

# 19. check if one is the complement of the other
                                  # keys are unique
bases = {'A':'T', 'T':'A', 'G':'C', 'C':'G'} # '' for all of them because they are strings

def complementary(seq1, seq2):
    list_of_alignmentsymbols=[]
    mismatches=0
    for i in range(len(seq1)):
        seq2base = seq2[i]
        if seq1[i] == bases[seq2base]:
            list_of_alignmentsymbols.append('|')
        else:
            list_of_alignmentsymbols.append('X')
            mismatches=mismatches + 1
    result =''.join(list_of_alignmentsymbols) #must be at the level of the for to be outside the loop
    return result, mismatches   

seq1='ATTCGTAT' #input('Please give me seq1')
seq2='TAGGAATT' #input('Please give me seq2')

if len(seq1) == len(seq2):
    alignmentsymbols = complementary(seq1, seq2)
    print("same length, alignment may be done")
    print(seq1)
    print(alignmentsymbols[0])
    print(seq2) 
    print('The number of mismatches is: ', alignmentsymbols[1])
else: 
    print('No alignment possible') #  returns nothing, exits funciton, stopps working
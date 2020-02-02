#18. print 3 rows: the first and the third for the sequences, 
#the second one should contain “|” if the bases are complementary, “X” if not. Example:
#ATTCGT
#||X|X|
#TAGGAA
a="ATTCGT"
la=len(a)
b="TAGGAA"
lb=len(b)
def comp(seq1,seq2):
    compl=[]

    for i in range(len(seq1)):
        if (seq1[i] =='A' and seq2[i] == 'T') or (seq1[i] =='T' and seq2[i] == 'A') or (seq1[i] =='G' and seq2[i] == 'C') or(seq1[i] =='C' and seq2[i] == 'G'):
            compl.append('|')
        else: 
            compl.append('X')
    return ''.join(compl)

print(a)
print(comp(a, b))
print(b)

# 22. Modify the program from point 20 or 21 in order to print also the number of non complementary positions (in the given example: 2)

#18. print 3 rows: the first and the third for the sequences, 
#the second one should contain “|” if the bases are complementary, “X” if not. Example:
#ATTCGT
#||X|X|
#TAGGAA
a="ATTCGT"
la=len(a)
b="TAGGGT"
lb=len(b)
def comp(seq1,seq2):
    compl=[]
    num=0
    for i in range(len(seq1)):
        if (seq1[i] =='A' and seq2[i] == 'T') or (seq1[i] =='T' and seq2[i] == 'A') or (seq1[i] =='G' and seq2[i] == 'C') or(seq1[i] =='C' and seq2[i] == 'G'):
            compl.append('|')
        else: 
            compl.append('X')
            num=num+1
    # print(num)
    return ''.join(compl), num# join works only on strings
    
print(a)
res= comp(a, b)
print(res[0])
print(b)
print("number of mismatches:", res[1])
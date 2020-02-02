# 21. rewrite the program from steps 18 to 20 so that it works for reverse complement (i.e. the user types the strings “ATTCGT” and “AAGGAT” and she gets the previous example as result)
#18. print 3 rows: the first and the third for the sequences, 
#the second one should contain “|” if the bases are complementary, “X” if not. Example:
#ATTCGT
#||X|X|
#TAGGAA
# now check if the first string is the reverse compliment of the other
#[i] and the other one must start at -1
a=input('Give me sequence 1 in capitals')
b=input("Give me another sequence 2 in capitals")
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

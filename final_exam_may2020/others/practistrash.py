difficultlist = ['>tr|Q9IQN3|Q9IQN3_9HIV1 Protein Rev (Fragment) OS=Human immunodeficiency virus 1 OX=11676 GN=rev PE=4 SV=1', 'PPPSSEGTRQARRNRRRRWRERQRQIRRISGWILSNHLGGLTEPVPLQLPPLERLTLDCN', 'EDCGTSGTQGVGSPQIPVESPTVLESGTKE', '>sp|O95218|ZRAB2_HUMAN Zinc finger Ran-binding domain-containing protein 2 OS=Homo sapiens OX=9606 GN=ZRANB2 PE=1 SV=2', 'MSTKNFRVSDGDWICPDKKCGNVNFARRTSCNRCGREKTTEAKMMKAGGTEIGKTLAEKS', 'RGLFSANDWQCKTCSNVNWARRSECNMCNTPKYAKLEERTGYGGGFNERENVEYIEREES', 'DGEYDEFGRKKKKYRGKAVGPASILKEVEDKESEGEEEDEDEDLSKYKLDEDEDEDDADL', 'SKYNLDASEEEDSNKKKSNRRSRSKSRSSHSRSSSRSSSPSSSRSRSRSRSRSSSSSQSR', 'SRSSSRERSRSRGSKSRSSSRSHRGSSSPRKRSYSSSSSSPERNRKRSRSRSSSSGDRKK', 'RRTRSRSPERRHRSSSGSSHSGSRSSSKKK', '']
difficultlist


saveseq = []
easystring = ''
seq1 = ''
seq2=''
for i in range(len(difficultlist)):
    easystring += difficultlist[i] # string without newlines now I can use the method split() again
    seqlist = easystring.split('>', 2) #splits into list of 3 items [0]='' [1]=seq1 [2]=seq2 (remember to test if it also works on file with more than 2 seq)
    print(seqlist[1]) 
          
print(easystring)
print(seqlist)


#     if difficultlist[i].startswith('>') != True:
#         saveseq.append(difficultlist[i])
# print(saveseq)
        
my_list = ["Hello", "world"]
print(str.join('-', my_list)) 
#     return filist

# def split_any_fasta(fastafile):
#     filist=[]
#     with open('./'+fastafile, 'r') as rfile:
#         for line in rfile:
#             filist.append(line.split("\n"))
#         print(filist)
#     return filist

# def list_to_string(filist):
#     stringed = ''
#     for i in range(len(filist)):
#         for j in range(len(filist)):
#         if str(filist[i][j].startswith('>')) == True:
#             continue
#         else:
#             print(filist[i][j])

# list_to_string(listoflists)


# def fasta_to_string(fastaf):
#     with open('./'+fastaf, 'r') as rfile:
#         aaline=''
#         seq1=''
#         seq2=''
#         for line in rfile:
#             if line.find(' ') != None:
#                 continue
#             else:
#                 aaline = rfile.readline()
#             print(aaline)

#     return aaline

# fi = "Q9IQN3.fasta" 
# print(fasta_to_string(fi))      
# #return (seq1, seq2)

# #         le = len(rfile.readlines())
# #         for line in range(1, le):
# #             if line != '>':
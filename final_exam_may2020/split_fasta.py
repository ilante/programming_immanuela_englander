# a) final version
# Thoughts
# - use either .readlines() to generate string of entire file and then .split('>')
# - or try with a loop that skipps the line containing '>' and saves the rest 

# Pseudocode
# general steps:
# - open file
# - read file
# - split the file to be able into 2 sequences preferably 2 lists that each contain one sequence
# - get rid of the header
# - keep the sequence only
# - get rid of the '\n' character
# - put each seq into variable
# - close file (not necessary if use ```with open()``` )
# - return tuple

def split_fasta(fastafile): 
    '''Function takes as input a fasta file containing *EXACTLY* 2 sequences. 
    It extracts the amino acid sequences and puts them into the variables
    seq1 and seq2 which are returned as a tuple (seq1, seq2)'''
    seq1 = '' #defining both variables now so they can be returned later
    seq2 = ''
    with open('./'+fastafile, 'r') as rfile: #open the fastafile
        allines = rfile.read()               # .read() returns the whole file as string
        newlist = allines.split(">")         # splitting the string into list of 3 items 
        seq1string =  newlist[1]             # seq1string takes item[1] of the newlist which is seq1 incl header
        seq2string =  newlist[2]             # seq2string takes item[2] of the newlist which is seq1 incl header
        liseq1 = seq1string.split("\n")      # removing the '\n' characters so the strgs can be joined later.
        liseq2 = seq2string.split("\n")
        noheader_list1=liseq1[1:]                 # noheaderX is the amino acid sequence alone
        noheader_list2=liseq2[1:]
        seq1 = str.join('', noheader_list1)       # joining the list of aa into string and putting it into the variable seq1, seq2
        seq2 = str.join('', noheader_list2)
    return (seq1, seq2)                      #returnin tuple with both sequences
         
seqtuple = split_fasta("Q9IQN3.fasta") #calling the funciton on the file that contains 2 seqs
print(seqtuple) #Printing the tuple see if it works
seq1, seq2 = seqtuple # unpacking the tuple
print("This is sequence 1 :\n",seq1, "\nThis is sequence 2 :\n",seq2) # printing each seq 


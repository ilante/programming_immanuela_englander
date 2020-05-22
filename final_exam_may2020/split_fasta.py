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

b)
# - try on tinymatrix.txt so its easier to build and expand later

#  ```

#    A  R  N  D  
# A  4 -1 -2 -2  
# R -1  5  0 -2 
# N -2  0  6  1 
# D -2 -2  1  6 


# ```

# make one fct that makes list of txt file:
# - open and .readlines() entire file: the method gives me a list where each item is one row.
# - name of row i (each item of list)
# - name of col j (inner indices)
# - I dont need the first row i=0 as it is exactly the same as [0][i] vertical down.
# - need to make a nested loop to do each against each:


def subsmat_from_txt(filename):
    '''Take as input a filename (must be written between '') of a square matrix does not contain a header. 
    It returns a substitution matrix. '''
    scoringmatrix_dict = {} #blosumdictionary
    pairli=[]
    
    with open(filename, 'r') as rfile:
        pairlist = []
        resilist = rfile.readline().rstrip().split() # creates list of all 20 residues.
        for i in range(len(resilist)):
            pair='' # creating loop to enable pairing the residues 'AA':, 'AR':...
            for j in range(len(resilist)):
                pair = resilist[i] + resilist[j]
                pairlist.append(pair) 
        # print(pairlist) # now I know I have a list that has all the keys. And every 20 items - so at item 21 Im in a new line of the matrix. At 41 in the line below that and at 61 below that.... So now I can add the values according to their postion in the txt.

        scorli = []
        numscoreli = []
        for k in range(1, len(resilist)+1): # index 0 is letters only - so I skip it. But need to add 1 otherwise last value would be lost. So all XV and VX values...
            full_list = rfile.readline().rstrip().split()
            scorli = full_list[1:] #now I know I have a list whose first character can be ommitted because its just the aa.
            for el in range(len(resilist)): # the list contains strings - need to generate integers.
                num_score = int(scorli[el])
                numscoreli.append(num_score) #numscoreli has the same layout as pairlist matching indecis can be paired as key and value:
        for l in range(len(pairlist)):
            scoringmatrix_dict[pairlist[l]] = numscoreli[l]
        return scoringmatrix_dict
    
# matrix = subsmat_from_txt("tinymatrix.txt")  
# print(matrix)
# print(len(matrix)) # 4*4 = 16
###################################################################################################
#it works on the tinymatrix.txt lets try it on the blosum50
blosum50 = subsmat_from_txt("blosum50.txt")
print(blosum50)
print(len(blosum50)) # checking the lenght to see if I managed to put all keys and values 20 * 20 = 400
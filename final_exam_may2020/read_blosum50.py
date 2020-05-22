def subsmat_from_txt(filename):
    '''Take as input a filename (must be written between '') of a matrix does not contain a header. 
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
    
matrix = subsmat_from_txt("tinymatrix.txt",)
print(matrix)    

matrix = subsmat_from_txt("blosum50.txt")
print(matrix)
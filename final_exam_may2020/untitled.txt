# b)
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
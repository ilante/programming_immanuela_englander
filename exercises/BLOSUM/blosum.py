# """

# BLOSUM50

# """
#    A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V
# A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0
# R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3
# N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3
# D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3
# C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
# Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2
# E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2
# G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3
# H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3
# I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3
# L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1
# K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2
# M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1
# F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1
# P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2
# S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2
# T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0
# W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3
# Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1
# V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4

# generate keys so just read firstline 2
# create a list of keys AA
# AA.append(value of key)
# blosum_dict={}

# open_read_file = open("./blosum50.txt", "r")
# amino_acids = open_read_file.readline()
# aa_list = amino_acids.split()
# #print(aa_list)
# blosum_dict[aa_list]=


filepath = "./blosum50.txt"
def matrix_to_dic(filepath): #takes the filepath as input
    fileopen = open(filepath, "r")
    aminoacid_list = fileopen.readline().rstrip().split() #readline reads ONLY firstline, rstrip removes spaces inbetween lines, split() on whitespaces.
    score_list = [] #make an empty list
    for line in fileopen: # for each line in the file
        score_list.append(line.rstrip().split()[1:]) # to_list_named_here.append(
    # print(score_list)
    fileopen.close() # good habit to save and close the file (even though i dont change it)
    
    blosum_score_dic = {}
    
    for i in range(len(aminoacid_list)): # for i in range(20) range gives numbers so i is a number.
#         print(i)
# matrix_to_dic(filepath)
        for j in range(len(aminoacid_list)): #
            current_key = aminoacid_list[i] + aminoacid_list[j] #current key is the aalist at index [i] add aalist at index [j] 
            blosum_score_dic[current_key] = int(value_list[i][j]) # nameofdict[keytobeadded]=value to be added
    return blosum_score_dic #return it so you can use it in the next function.

def score_seq(seq1, seq2, blosum_score_dic): # define a new fct
    total_score = 0 # define variable of the score 
    for i in range(len(seq1)): # i is a number because it was defined by len 
        current_pair = seq1[i] + seq2[i] #concuttinates letters of seq1 in pos i and letters of seq2 in same postion.
        current_score = blosum_score_dic[current_pair] # save into the variable the value of the key from 'current-score' from dict blo_sco[key] 
        total_score += current_score
    return total_score


matrix_file = "../data/blosum.txt"
sample_seq1 = "ARND"
sample_seq2 = "ARND"
blosum = matrix_to_dic(matrix_file)
score = score_seq(sample_seq1, sample_seq2, blosum)
print(score)
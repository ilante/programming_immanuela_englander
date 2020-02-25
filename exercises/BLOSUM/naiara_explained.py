#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:18:20 2020

@author: naiara modyfied by ila

NEEDLEMAN-WUNSCH - Global alignment WITH GAPS
"""
import matrices

def global_alignment(seq1, seq2, substitutionMatrix, gap_penalty):
    """ Does global alignment employing dynamic programming with help of the Needleman-Wunsch algorithm. Needs 2 sequences, one scoring matrix such as BLOSUM or PAM and a gap penalty as input. It creates matrix S (containing    the score) and the path matrix P (containing the path for backtracking). It returns both S and P and the maximum score."""
    number_of_rows_lencol = len(seq1) + 1 # M[0][0] filled with 0 plus seq1 (is on the "vertical dimension" of the matix) and determines the number of rows. This also determines the lenght of each column
    number_of_columns_lenrows = len(seq2) + 1 # Here its M[0][0] filled with 0 plus seq2 across "horizontal dimension" that determines the length of each row plus 

    # #  0  s  e  q  2        illutstrates how len(seq2)+1 determines the number of columns (5) AND the length of each row
    # 0  0 -2 -4 -6 -8       and len(seq1)+1 dictates the number of rows AND the lenght of each column
    # s -2 x  x  x   x
    # e -4 x  x  x   x
    # q -6 x  x  x   x
    # 1 -8 x  x  x   x

    # Generate matrices S and P and dimensions number_of_rows_lencol * number_of_columns_lenrows. Fills it with 0 for now.
    S = [[0] * number_of_columns_lenrows for x in range(number_of_rows_lencol)]
    P = [[0] * number_of_columns_lenrows for x in range(number_of_rows_lencol)]
    
    # Fill the first column of the matrices S (score) and P (path).
    for i in range(number_of_rows_lencol):
        S[i][0] = gap_penalty * i # to obtain all the gap penalties you need to multiplicate with the iteration
        P[i][0] = 'u' # indicates up
        
    # Fills first row of the each matrix S and P. Now i is fixed and j iterates.
    for j in range(number_of_columns_lenrows):
        S[0][j] = gap_penalty * j # to obtain all the gap penalties you need to multiplicate with the iteration
        P[0][j] = 'l' # indicates left
        
    # Fills the remaining cols and rows of each matrix starting at index 1 (because 0 was filled above)
    for i in range(1, number_of_rows_lencol): # Columns
        for j in range(1, number_of_columns_lenrows): # Rows
            
            sDiagonal = S[i-1][j-1] + substitutionMatrix[seq1[i-1] + seq2[j-1]] # Previous value in the diagonal + score of match or mismatch
            sColumn = S[i-1][j] + gap_penalty # Previous value in the column + gap
            sRow = S[i][j-1] + gap_penalty # Previous value in the diagonal + gap
            
            # Obtain the maximun value
            max_score = max(sDiagonal, sColumn, sRow)
            
            # Add u = up, l = left and d = diagonal in the matrix P
            if max_score == sDiagonal:
                P[i][j] = "d" # d, represents diagonal
            elif max_score == sColumn:
                P[i][j] = "u" # u, represents column (up)
            else:
                P[i][j] = "l" # l, represents row (left)
                
            S[i][j] = max_score # strore the max_score in the matrix S in position Sij

    return S,P

S, P = global_alignment('ADCDN', 'AWCN', matrices.blosum62, -4)

print(S)
print('dir')
print(P)

for row in S:
    for num in row: # each number in a row
        print(num,'\t', end='')
    print('') # newline when we finish printing a row

for dir in P:
# unpack
    for letter in dir:
        print(letter+'\t', end='')
    print('')

def best_alignment(seq1, seq2, S, P):
    """ The function aligns seq1 to seq2 using P matrix. 
    The score will be extracted from the matrix S, which stores all the maxima of the alignment. "best_alignment" returns the template (seq1), target (seq2) including eventual gaps in the two AND best score"""
    
    i = len(P) - 1; j = len(P[0]) -1 # Get the index of the last position on the matrix. Indicates start of backtracking
    template = ""; target = ""; score = S[i][j] # The last position of the matrix S is the best score in NW with gaps
    while i + j != 0: #because only if both are 0 it should stop
        if P[i][j] == "d": # if from diagonal = match or mismatch
            template += seq1[i - 1] # Add to the string template the letter of the sequence 1
            target += seq2[j - 1] # Add to the string template the letter of the sequence 2
            i -= 1 # decrement i for one to continue backtracking
            j -= 1 # same for j
        elif P[i][j] == "u":
            template += seq1[i - 1] # Insert in template the letter of the sequence 1
            target += "-" # Inserts a gap 
            i -= 1
        else:
            template += "-" #Symbolizes insertion of a gap
            target += seq2[j - 1] # Insert in template the letter of the sequence 2
            j -= 1
            # Use gaps when the movement is to left or up, we are add a gap "-". It means no match.
    return template, target, score

# def represent_alignment(template, target, score):            
#     """ Print the template (sequence 1) and the target (sequence 2) representing the best alignment and the score"""
#     template = template[::-1] # Reverse template
#     target = target[::-1] # Reverse target
#     print("Seq1:", template)
#     print("Seq2:", target)
#     print("Score:", score)
    
# def obtain_data():
#     """ Function to read the seq1, seq2 and the substitutionMatrix dictionary from the file input_data.py """
#     import input_data
#     dic = input_data.BLOSUM52
#     seq1 = input_data.seq1
#     seq2 = input_data.seq2
#     return seq1, seq2, dic

# if __name__ == "__main__":
#     seq1, seq2, BLOSUM52 = obtain_data() # Sequences without gaps and dictionary BLOSUM52
#     gap_penalty = -2 # Use the normal gap_penalty that we use in class, in the exam is not specificed
#     F, P = global_alignment(seq1, seq2, BLOSUM52, gap_penalty)
#     template, target, score = best_alignment(seq1, seq2, F, P)
#     represent_alignment(template, target, score)
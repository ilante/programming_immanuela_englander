#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:18:20 2020

@author: naiara modyfied by ila

NEEDLEMAN-WUNSCH - Global alignment WITH GAPS
"""
import matrices

def glob_al_NW(seq1, seq2, substitutionMatrix, gap_penalty):
    """ Does global alignment employing dynamic programming with help of the Needleman-Wunsch algorithm. Needs 2 sequences, one scoring matrix such as BLOSUM or PAM and a gap penalty as input. It creates matrix S (containing    the score) and the path matrix P (containing the path for backtracking). It returns both S and P and the maximum score."""
    num_rows = len(seq1) + 1 # M[0][0] filled with 0 plus seq1 (is on the "vertical dimension" of the matix) and determines the number of rows. This also determines the lenght of each column
    num_cols = len(seq2) + 1 # Here its M[0][0] filled with 0 plus seq2 across "horizontal dimension" that determines the length of each row plus 

    # #  0  s  e  q  2        illutstrates how len(seq2)+1 determines the number of columns (5) AND the length of each row
    # 0  0 -2 -4 -6 -8       and len(seq1)+1 dictates the number of rows AND the lenght of each column
    # s -2 x  x  x   x
    # e -4 x  x  x   x
    # q -6 x  x  x   x
    # 1 -8 x  x  x   x

    # Generate matrices S and P and dimensions num_rows * num_cols. Fills it with 0 for now.
    S = [[0] * num_cols for x in range(num_rows)]
    P = [[0] * num_cols for x in range(num_rows)]
    
    # Fill the first column of the matrices S (score) and P (path).
    for i in range(num_rows):
        S[i][0] = gap_penalty * i # to obtain all the gap penalties you need to multiplicate with the iteration
        P[i][0] = 'u' # indicates up
        
    # Fills first row of the each matrix S and P. Now i is fixed and j iterates.
    for j in range(num_cols):
        S[0][j] = gap_penalty * j # to obtain all the gap penalties you need to multiplicate with the iteration
        P[0][j] = 'l' # indicates left
        
    # Fills the remaining cols and rows of each matrix starting at index 1 (because 0 was filled above)
    for i in range(1, num_rows): # indexes of 'outer list' iterates through the 'lines of the matrix'
        for j in range(1, num_cols): # Rows
            
            sDiagonal = S[i-1][j-1] + substitutionMatrix[seq1[i-1] + seq2[j-1]] # Previous value in the diagonal + score of match or mismatch
            s_Top = S[i-1][j] + gap_penalty # Previous value in the column + gap
            s_Left = S[i][j-1] + gap_penalty # Previous value in the diagonal + gap
            
            # Obtains the maximun value
            max_score = max(sDiagonal, s_Top, s_Left)
            
            # Fills the path matrix with directional indication u = up, l = left and d = diagonal in the matrix P
            if max_score == sDiagonal:
                P[i][j] = "d" # d, represents diagonal
            elif max_score == s_Top:
                P[i][j] = "u" # u, represents column (up)
            else:
                P[i][j] = "l" # l, represents row (left)
                
            S[i][j] = max_score # strore the max_score in the matrix S in position Sij

    return S,P

# S, P = glob_al_NW('ADCDN', 'AWCN', matrices.blosum62, -4) # variable S and P are defined and hold now whatever the funciton
# # glob_al_NW returns.

# print(S)
# print('dir')
# print(P)

# for row in S:
#     for num in row: # each number in a row
#         print(num,'\t', end='')
#     print('') # newline when we finish printing a row

# for dir in P:
# # unpack
#     for letter in dir:
#         print(letter+'\t', end='')
#     print('')

def best_alignment(seq1, seq2, S, P):
    """ The function aligns seq1 to seq2 by backtracking using P matrix. 
    The score is obtained from the matrix S, which stores all the maxima of the alignment. "best_alignment" returns the template (seq1), target (seq2) including eventual gaps AND best score"""
    
    i = len(P) - 1; j = len(P[0]) -1 # To get the index of the last position on the matrix. Indicates start of backtracking
    template_l = ""; target_u = ""; score = S[i][j] # The last position of the matrix S is the best score in NW with gaps
    while i + j != 0: #because only if both are 0 it should stop
        if P[i][j] == "d": # if from diagonal = match or mismatch
            template_l += seq1[i - 1] # Concattinate corresponding part of seq1 to the string called template
            target_u += seq2[j - 1] # Concattinate corresponding part of seq2 to the string called template.
            i -= 1 # decrement i for one to continue backtracking
            j -= 1 # same for j
        elif P[i][j] == "u":
            template_l += seq1[i - 1] # Insert in template the letter of the sequence 1
            target_u += "-" # Inserts a gap 
            i -= 1
        else:
            template_l += "-" #Symbolizes insertion of a gap
            target_u += seq2[j - 1] # Insert in template the letter of the sequence 2
            j -= 1
            # Use gaps when the movement is to left or up, we are add a gap "-". 

    return template_l, target_u, score

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
#     F, P = glob_al_NW(seq1, seq2, BLOSUM52, gap_penalty)
#     template, target, score = best_alignment(seq1, seq2, F, P)
#     represent_alignment(template, target, score)
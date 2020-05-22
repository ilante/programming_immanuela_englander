'''Final version Smith Waterman (Examples: p 95/96 Concepts in Bioinformatics and Genomics, J. Momand, A. McCurdy)
Developed by Temple Smith and Michael Waterman in 1981. We need to make three changes to the N-W program.
1) Modifying the equation by adding a fourth option: 0 for the calculation of S i, j. 
Thus no element can be less than zero. 
2) Traceback is started from the highest value of S i, j and continues until 0 is found.
once 0 is found the traceback stops. This point is the end of the seuquece alignment.

SW_alignment(Input: Sequence1, Sequence 2, Substitution_Matrix_Dictionary, gap_penalty)
- define matrix dimension according to length of S1 and S2 PLUS one to account for the empty field before each sequence starts (does not contain a letter:)

* *    H    E    A    G    A    W   G    H   E    E
* 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0
P 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0
A 0,   0,   0,   5,   0,   5,   0,   0,   0,   0,   0
W 0,   0,   0,   0,   2,   0,  20,  12,   4,   0,   0
H 0,  10,   2,   0,   0,   0,  12,  18,  22,  14,   6
E 0,   2,  16,   8,   0,   0,   4,  10,  18,  28,  20
A 0,   0,   8,  21,  13,   5,   0,   4,  10,  20,  27
E 0,   0,   6,  13,  18,  12,   4,   0,   4,  16,  26

- initialize 0 matrix S for score;
- initialize * matrix P for the path 
- fill first column and first row of S with the gap penalty
- fill first culumn and first row of P with indicators for direction 'h'orizontal 'v'ertical
- nested for-loop to fill the remaining positions of each matrix
  remember: both ranges START at 1 because first r & c are filled already!!!
- use while loop to ensure it iterates ONLY until it hits ZERO.
- Traceback startes at exactly the postion of the HIGHEST value:
  if Diagonal: two sequences are aligned and assigned their match score
  if Vertical: gap must be introduced in the sequence from up.
  if Horizontal: gap must be introduced in the sequence from the left.


- OUTPUT: the function must 
  return S and P.

It is important to keep in mind that MORE than one alignment can be 'best'.'''

# 3) Elements of the top row (i=0) and first column (j=0) are all set to 0.

from blo_fifity import blosum50
import sys

def smith_waterman_alignment(seq1, seq2, scoringMtrx, gap_penalty):
    ''' Function calculates the global dynamic programming (scoring) matrix S based 
    on the Smith- Waterman algorithm and the associated traceback matrix P. Input:
    seq1, seq2, BLOSUM50 matrix and the gap penalty as input. It returns S and P.'''
    num_rows = len(seq1) + 1 # number of rows or the length of each column
    num_cols = len(seq2) + 1 # number of columns or the length of each row

    # 1 . initialize one Matrix for the score: S and one for the path P:
    # S: zero matrix of dimensions num_rows * num_cols (m * n)
    # P: asterisk matrix of dimensions num_rows * num_cols (m * n)

    S = [[0] * num_cols for m in range(num_rows)] 
    P = [['*'] * num_cols for m in range(num_rows)] 

    # 2. fill first column and first row
    # S: with gap penalty
    # P: with directions: for 1st row "h" ; for 1st col: "v"

    for i in range(num_rows):       # REMEMBER: can only iterate in RANGE(...) TypeError: 'int' object is not iterable
        P[i][0] = 'v' # filling first col with letter indicating vertical move up is saved in P matrix

    for j in range(num_cols):       # 
        P[0][j] = 'h' # filling first row with letter indicating horizontal move left is saved in P matrix

    # 3. Fill inn scores into remaining fields of S 
    # since i and j 0 are filled in already: we start from i and j ONE  !!!

    for i in range(1, num_rows):       # because 0 is filled already range must start at 1
        for j in range(1, num_cols):   # same here 0 is filled above so range starts one later

            Diagonal_score = S[i-1][j-1] + scoringMtrx[seq1[i-1] + seq2[j-1]] #Store diagonal score in variable
            Vertical_score = S[i-1][j] + gap_penalty  #Store vertical score in variable
            Horizontal_score= S[i][j-1] + gap_penalty #Store horizontal score in variable

            # 4. find maximum of the score to determine direction (diagonal 'd', vertical 'v' or horizontal 'h'

            max_score = max(Diagonal_score, Vertical_score, Horizontal_score, 0) #for SW need to include 0 into the maximum function !!!

            # 5. fill inn directional information into the open fields of the P matrix
            
            if max_score == Diagonal_score:
                P[i][j] = 'd'    # letter indicating diagonal move up is saved in P matrix
            elif max_score == Vertical_score:
                P[i][j] = 'v'    # letter indicating vertical move up is saved in P matrix
            else:
                P[i][j] = 'h'    # letter indicating horizontal move corssover is saved in P 

                                 # 6. store value of max_score in corresponding field of S[i][j]:
            S[i][j] = max_score
    
                                 # 7. return both matrices
    return S, P     # INDENTATION needs to be outside of both loops!!!

def max_val_mat(M):
    ''' The function takes as input a matrix. It returns the maximum value found in the matrix and its position M_i,j '''
    max_val = M[0][0]                  # starts at top left corner
    pos_i = 0                          # to later store the value of i of the best field
    pos_j = 0                          # to later store the value of j of the best field
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] > max_val:
                max_val = M[i][j]
                pos_i = i
                pos_j = j
    return pos_i, pos_j, max_val

def many_val_mat(M, val):
    ''' The function takes as input a matrix and a value. It returns a list of the positions with the same value M_i,j '''
    same_val_list = []                 # to store position(s) of values eqal to val
    pos_i = 0                          # to later store the value of i of the best field
    pos_j = 0                          # to later store the value of j of the best field
    for i in range(len(M)):         
        for j in range(len(M[0])):
            if M[i][j] == val:         # if the value in the position is equal: store the positon in the same_val_list = []
                same_val_list.append((i, j))
    return same_val_list

# Pseudocode:
#     - function takes as input s1 s2, ScoringMatrix S and PathMatrix P.
#     - need to put the maximum value from the S matrix into the variable i, j and max I can do that by calling my function max_val_mat() and pass S.
#     - define variables for the strings of the s1 and s2. REMEMBER backtracking reads backwards. They need to be flipped later.
#     - use a while loop to track back until a 0 is met.
#     - retrieve letter of the sequence by acessing the dict and save to the variable
#     - decrememnt i and j according to the situation (d, v, h)
#     - flip both s1 and s2 so they are read in the right direction
#     - return s1, s2 and score

def traceback_SW_best_alignment(seq1, seq2, S, P):
    ''' Function performes back tracking to determine the best alignment of template (seq1) and target (seq2). The moves are either:
    - diagonal: match/mismatch 
    - vertical/top:       gap in sequence 1
    - horizontal/left:     gap in sequence 2
    Function returns template_seq1, target_seq2 and score'''
    
    i,j,max = max_val_mat(S)                # assigning variables to each output of the function. Indeces i,j of max value = starting point of traceback
    
    score = S[i][j]                         # 'score' the highest value
    rev_template_seq1 = ''                  # 'rev_...' because by backtracing we first obtain each sequence backwards so we need to flip it again
    rev_target_seq2 = '' 
   
    while S[i][j] != 0:                     # loop continues until it encounters ZERO
        if P[i][j] == 'd':                  # match or mismatch from diagonal
            rev_template_seq1 += seq1[i-1]
            rev_target_seq2 += seq2[j-1]
            i -= 1                     
            j -= 1                          # decrement both i and j                    
            
        elif P[i][j] == 'v':           
            rev_template_seq1 += '-'        # vertical: from top: gap is introduced in seq1
            rev_target_seq2 += seq1[i-1]
            i -= 1                          # Here ONLY i is decremented   
        else:                            
            rev_template_seq1 += seq2[j-1]
            rev_target_seq2 += '-'          # so if P[i][j] was from 'h' horizontal move --> introduce gap into seq2
            j -= 1                          # Here ONLY j is decremented  

        # print("i", i, 'j', j, S[i][j])    # testprint
                                                    
        template_seq1 = rev_template_seq1[::-1] # reverse needs to be flipped : turn around seq1
        target_seq2 = rev_target_seq2[::-1]     # flip seq2
    return template_seq1, target_seq2, score    # return the Sequence 1, Sequence 2 and the Score

################ CHECKING ###############################################
# try it with example from Concepts in Bioinformatics and genomics page 96 
# and veryfy with https://gtuckerkellogg.github.io/pairwise/demo/ 
# >
s1 = 'PAWHEAE' ; s2 =  "HEAGAWGHEE"
S, P = smith_waterman_alignment(s1, s2, blosum50, -8) # unpacked S and P from function global_alignment
print(max_val_mat(S), 'i, j, and Maxvalue')

print("This is the Path Matrix, holding the path for backtracking")
for line in P:
    print(line)
print('')
print("This is the Score Matrix, holding the score of each pair")    
for line in S:
    print(line)
# call function traceback_best_alignment OBVIOUSLY with same parameters
# and unpack what it returns: >> template_seq1, target_seq2, score
template_seq1, target_seq2, score = traceback_SW_best_alignment(s1, s2, S, P)

print('The alinment:')
print(template_seq1)
print(target_seq2)
print('the score is ', score)

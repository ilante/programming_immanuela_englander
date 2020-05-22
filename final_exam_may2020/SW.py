def global_alignment(seq1, seq2, scoringMtrx, gap_penalty):
    ''' Function calculates the global dynamic programming (scoring) matrix S based 
    on the Smith- Waterman algorithm and the associated traceback matrix P. Input:
    seq1, seq2, BLOSUM50 matrix and the gap penalty as input. It returns S and P.'''
    num_rows = len(seq1) + 1 # number of rows or the length of each column
    num_cols = len(seq2) + 1 # number of columns or the length of each row

    # 1 . initialize one M for the score: S and one for the path P:
    # S: zero matrix of dimensions num_rows * num_cols (m * n)
    # P: asterisk matrix of dimensions num_rows * num_cols (m * n)

    S = [[0] * num_cols for m in range(num_rows)] 
    P = [['*'] * num_cols for m in range(num_rows)] 

    # 2. fill first column and first row
    # S: with gap penalty
    # P: with directions: for 1st row "h" ; for 1st col: "v"

    for i in range(num_rows):       # REMEMBER: can only iterate in RANGE(...) TypeError: 'int' object is not iterable
        S[i][0] = 0 # gap_penalty * i
        P[i][0] = 'v' #vertical

    for j in range(num_cols):       # again REMEMBER can only iterate on RANGE(...) TypeError: 'int' object is not iterable
        S[0][j] =  0 #gap_penalty * j
        P[0][j] = 'h' #horizontal

    # 3. Fill inn scores  remaining fields of S 
    # since i and j 0 are filled in already: we start from i and j ONE  !!!

    for i in range(1, num_rows):       # RANGE(1, num_rows)
        for j in range(1, num_cols):   # RANGE(1, num_cols) 

            Diagonal_score = S[i-1][j-1] + scoringMtrx[seq1[i-1] + seq2[j-1]] 
            Vertical_score = S[i-1][j] + gap_penalty 
            Horizontal_score= S[i][j-1] + gap_penalty 

            # 4. find maximum of the score to determine direction (diagonal 'd', vertical 'v' or horizontal 'h'

            max_score = max(Diagonal_score, Vertical_score, Horizontal_score, 0) #for NW need to include 0 into the max fct. !!!

            # 5. fill inn directional information into the P matrix
            if max_score == Diagonal_score:
                P[i][j] = 'd'
            elif max_score == Vertical_score:
                P[i][j] = 'v'
            else:
                P[i][j] = 'h'      # Horizontal_score

            # 6. store value of max_score in corresponding field of S[i][j]:
            S[i][j] = max_score
    
            # 7. return both matrices
    return S, P     # INDENTATION needs to be outside of both loops

def max_val_mat(M):
    ''' The function takes a matrix as parameter. Returns its maximum value and its position M_i,j '''
    max_val = M[0][0]
    mi = 0
    nj = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] > max_val:
                max_val = M[i][j]
                mi = i
                nj = j

    return mi, nj, max_val


def traceback_SW_best_alignment(seq1, seq2, S, P):
    ''' Function performes back tracking to determine the best alignment of template (seq1) and target (seq2). 
    Function returns template_seq1, target_seq2 and score'''
    
    i,j,max = max_val_mat(S) # index of max value = starting point of traceback
    
    score = S[i][j]           # 'score' holds value of bottom right corner
    rev_template_seq1 = ''     # 'rev_...' because by backtracing we first obtain the reverse of each seq
    rev_target_seq2 = '' 
   
    while S[i][j] != 0:                  # loop continues until it encounters one of the margines
        if P[i][j] == 'd':             # match or mismatch from diagonal
            rev_template_seq1 += seq1[i-1]
            rev_target_seq2 += seq2[j-2]
            i -= 1                     # decrement both i and j 
            j -= 1
            
        elif P[i][j] == 'v':           # from top: gap is introduced in seq1
            rev_template_seq1 += '-'
            rev_target_seq2 += seq2[j-1]
            j -= 1                     # Here only j is decremented   
        
        else:                           # so if P[i][j] was from 'h' horizontal move --> gap in seq2
            rev_template_seq1 += seq1[i-1]
            rev_target_seq2 += '-'
            i -= 1                      # Here only j is decremented  
        
        # reverse needs to be corrected : turn around
        template_seq1 = rev_template_seq1[::-1]
        target_seq2 = rev_target_seq2[::-1]

        # return alignment and score
    return template_seq1, target_seq2, score    # INDENTATION after while is terminated !!!!

# try it with example from Concepts in Bioinformatics and genomics page 96 
# 
# >
s1 = 'PAWHEAE' ; s2 =  "HEAGAWGHEE"
S, P = global_alignment(s1, s2, blosum50, -8) # unpacked S and P from function global_alignment
print(max_val_mat(S), 'tadaaa')

for line in P:
    print(line)
for line in S:
    print(line)
# call function traceback_best_alignment OBVIOUSLY with same parameters
# and unpack what it returns: >> template_seq1, target_seq2, score
template_seq1, target_seq2, score = traceback_SW_best_alignment(s1, s2, S, P)
print(template_seq1)
print(target_seq2)
print('the score is ', score)

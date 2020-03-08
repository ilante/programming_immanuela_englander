import matrices

def global_alignment(seq1, seq2, scoringMtrx, gap_penalty):
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
        S[i][0] = gap_penalty * i
        P[i][0] = 'v'

    for j in range(num_cols):       # again REMEMBER can only iterate on RANGE(...) TypeError: 'int' object is not iterable
        S[0][j] = gap_penalty * j
        P[0][j] = 'h'

    # 3. Fill inn scores  remaining fields of S 
    # since i and j 0 are filled in already: we start from i and j ONE  !!!
    for i in range(1, num_rows):       # again REMEMBER can only iterate on RANGE(1, num_rows) TypeError: 'int' object is not iterable
        for j in range(1, num_cols):   # fourth time same mistake: iteration needs a RANGE of sth !!!! number alone doesnt work

            Diagonal_score = S[i-1][j-1] + scoringMtrx[seq1[i-1] + seq2[j-1]] # Previous value in the diagonal + score of match or mismatch
            Vertical_score = S[i-1][j] + gap_penalty # Previous value in the column + gap
            Horizontal_score= S[i][j-1] + gap_penalty # Previous value in the row + gap

            # 4. find maximum of the score to determine direction (diagonal 'd', vertical 't' or horizontal 'h'

            max_score = max(Diagonal_score, Vertical_score, Horizontal_score)

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

# time: 20 min

def traceback_best_alignment(seq1, seq2, S, P):
    ''' Function performes back tracing to determine the best alignment of template (seq1) and target (seq2). 
    Function returns template_seq1, target_seq2 and the score'''
    i = len(S)-1 ; j = len(S[i])-1 # IndexError: list index out of range 
    # REMEMBER to define it as len(S)-1 to stay in range
    # otherwise we start in S[i][j] that doesnt exist
    # #  0  s  e  q  2        illutstrates how len(seq2)+1 determines the number of columns (5) AND the length of each row
    # 0  0 -2 -4 -6 -8       and len(seq1)+1 dictates the number of rows AND the lenght of each column
    # s -2 x  x  x   x       
    # e -4 x  x  x   x       One must be substracted to get last index:
    # q -6 x  x  x   x
    # 1 -8 x  x  x   L       L is the last pos in S: S[5-1][5-1] 
    score = S[i][j] 
    rev_template_seq1 = '' ; rev_target_seq2 = '' 
    
    # 'score' holds value of bottom right corner
    # 'rev_...' because by backtracing we first obtain the reverse of each seq

    while i + j != 0:       # loop continues until it encounters one of the margines
        if P[i][j] == 'd':   # match or mismatch from diagonal
            rev_template_seq1 += seq1[i-1]
            rev_target_seq2 += seq2[j-2]

            # decrement both i and j !!!
            i -= 1
            j -= 1
        elif P[i][j] == 't':    # from top: gap is introduced in seq1
            rev_template_seq1 += '-'
            rev_target_seq2 += seq2[j-1]

            #decrement j only !!!
        
        else:  # so if P[i][j] was from 'l' horizontal move --> gap in seq2
            rev_template_seq1 += seq1[i-1]
            rev_target_seq2 += '-'

            # decrement i only !!!
            i -= 1

        # reverse needs to be corrected : turn around
        template_seq1 = rev_template_seq1[::-1]
        target_seq2 = rev_target_seq2[::-1]

        # return alignment and score
    return template_seq1, target_seq2, score    # INDENTATION after while is terminated !!!!

# try it with example from Concepts in Bioinformatics and genomics
# >
s1 = 'ADCDN' ; s2 =  "AWCN"
S, P = global_alignment(s1, s2, matrices.BLOSUM62, -4)

# unpacked S and P from function global_alignment

# call function traceback_best_alignment OBVIOUSLY with same parameters
# and unpack what it returns: >> template_seq1, target_seq2, score
template_seq1, target_seq2, score = traceback_best_alignment(s1, s2, S, P)
print(template_seq1)
print(target_seq2)
print('the score is ', score)




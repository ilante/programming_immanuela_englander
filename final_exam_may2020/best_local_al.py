# Pseudocode:
#     - function takes as input s1 s2, ScoringMatrix S and PathMatrix P.
#     - need to put the maximum value from the S matrix into the variable i, j and max I can do that by calling my function max_val_mat() and pass S.
#     - define variables for the strings of the s1 and s2. REMEMBER backtracking reads backwards. They need to be flipped later.
#     - use a while loop to track back until a 0 is met.
#     - retrieve letter of the sequence by acessing the dict and save to the variable
#     - decrememnt i and j according to the situation (d, v, h)
#     - flip both s1 and s2 so they are read in the right direction
#     - return s1, s2 and score

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
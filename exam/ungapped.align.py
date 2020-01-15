# ------------------------------------------------------------------------
# 2) Write a script that generates all the possible ungapped alignments of two sequences, scores them and identifies
# the best scoring ones.

# These are all the possible ungapped alingments of the two sequences: TCA and GA:

# --TCA  -TCA  TCA  TCA  TCA-  TCA--
# GA---  GA--  GA-  -GA  --GA  ---GA

# Using the following scoring scheme:

# score_matrix = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
#                 'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
#                 'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
#                 'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2}


# The best scoring alignment is:
# TCA
# -GA
# ------------------------------------------------------------------------
scoring_matrix = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
                'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
                'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
                'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2}

seq1 = 'TCA'
seq2 = 'GA'


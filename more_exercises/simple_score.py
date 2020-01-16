def score(seq1, seq2):
    score = 0
    for index in range(len(seq1)):
        if seq1[index] == seq2[index]:
            score += 1
        else:
            score += 0 
    return score
seq1='ACAG'
seq2='ACCA'
x=score(seq1, seq2)
print(x)
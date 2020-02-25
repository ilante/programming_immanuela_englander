# 24. Modify the previous programs in order to read the sequences from file, checking for each one with all the others of the same length for the one with the smallest number of non complementary positions. Print each string with its best match and score as in point 22.
# Example:
# Input file
# ATTCGT
# TAGGAA
# TCAGCA
# AAAAAAAAA
# TTTTTTTTT
# Result:
# ATTCGT and TCAGCA with 1 non complementary position
# TAGGAA and ATTCGT with 2 non complementary positions
# TCAGCA and ATTCGT with 1 non complementary position
# AAAAAAAAA and TTTTTTTTT
# TTTTTTTTT and AAAAAAAAA
# 25. Modify the previous programs so to write the results in a new file
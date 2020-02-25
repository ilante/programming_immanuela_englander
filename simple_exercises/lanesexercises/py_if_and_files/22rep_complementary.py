
# 22. Modify the program from point 18 in order to print also the number of non complementary positions (in the given example: 2)

one = input('Give me seqence please! ')
two = input('Give me another one. ')

# 17. check if one string is the complement of the other (i.e. “AC” and “TG” -> yes)
bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def complement(seq1, seq2, di):
    pattern = ''
    poscount = 0
    for i in range(len(seq1)): # to get the index we need the range of len seq1
        if seq1[i] == bases[seq2[i]]: # range starts at zero by default and doenst include last number
            pattern += '|'
            poscount += 1
        else:
            pattern += 'X'
    print(seq1)
    print(pattern)
    print(seq2)
    print('There are ', poscount, 'complementary pairs in the alignment.')

complement(one, two, bases)

# 23. Modify the previous programs in order to read the sequences from file, using them in pairs (i.e. first row with second row, third with fourth and so on) Note: each pair of strings must have the same length (i.e. first and second row must have the same length, for example 6, third and fourth row may have both length 9 etc)
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

#  Python-dictionaries

# 1. Create an empty dictionary
# 2. Use the dictionary to store the age of persons, and add three persons to the dictionary (with their age), including yourself
# 3. Find your age in the dictionary
# 4. Find the name of the youngest person
# 5. Find the age of the youngest person
# 6. Remove yourself from the dictionary
# 7. Compute the average age

#     Python-functions2

# 1. Define a function to compute the square of a number
# 2. Use the function to compute the square of all numbers of a given list
# 3. Define a function to check whether a number is even
# 4. Using functions from points 1. and 3., define a function that takes an integer and returns its square if it is even, the number itself otherwise
# 5. Take program 24. from the if-and-file section. Structure it in a suitable way using functions 

#     Python-recursion

# 1. Define the fibonacci function
# 2. Compute fibonacci(20), fibonacci(30) and fibonacci(35)
# 3. Define a recursive function to compute the function f defined by:
#    f(0) = 1
#    f(1) = 7
#    f(n) = n * f(n-2) if n>1
# 4. Define a recursive function to double all the elements of a list of integers
# 5. Define a recursive function to double all the elements of a list of integers until a 0 is found
# 6. Define a recursive function to compute the partial sums of a list of integers
# 7. Define a function to compute the permutations of a list

#     Python-while

# 1. Use a while loop to compute the sum of a list of integers
# 2. Use a while loop to compute the partial sums of a list of integers
# 3. Use a while loop to print all the characters of a string until you find two consecutive equal characters (which should not be printed). Is there any advantage of using a while loop instead of a for loop?
# 4. Ask numbers to the users until it inserts an even number. Print the number of tries.

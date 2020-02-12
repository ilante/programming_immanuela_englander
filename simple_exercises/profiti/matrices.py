import input_data
from input_data import align1 # to import the alignment
# print(align1)
from input_data import PAM250_dict # to import the dictionary
# print(PAM250_dict)
# print(len(align1[0]))
# print(len(align1[1]))
# both are the same size: I can only do it for seq of the same size

list_of_AA = []
if len(align1[0]) == len(align1[1]):
    # print('true')my code only will be for alignments of the same length
    for i in range(len(align1[0][::]):
        # for e in align1[1][::]:
        #     x = list_of_AA.append(i + e) #+ e)
        #     print(x)

############################################################################
# ON THE UPSIDE; AT LEAST I DIN NOT JUST DO IT IN GROUP WORK LIKE OTHERS...
############################################################################
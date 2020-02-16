
# 16. ask the user for two strings
# string1=input('please input a string ')
# string1=string1.upper()

# # print(string1)
# string2=input('please input a second string ')
# string2=string2.upper()

# print(string2)

di_seq ={"A":"T", "T":"A", "G":"C", "C":"G"}

# print(di_seq)
# print(di_seq["A"])
# for el in di_seq:
#     print(di_seq[el])
# 17. check if one string is the complement of the other (i.e. “AC” and “TG” -> yes)
def complement(s1, s2):
    if len(s1) == len(s2):
        print("strings of same length can be aligned")
    else:
        print("strings are not the same length")
    for i in range(len(s1)):
        char_template = s1[i]
        char_seq = s2[i]
        if char_template == di_seq[char_seq]:
            print("match")
        else:
            print('mismatch')

a, b = "ATG", "TAG"
complement(a, b)
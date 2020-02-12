# 1.13 Base complement
# Given a character a representing a DNA base (e.g. A, T, C, G), evaluate its complement. 

bas_dict={'a':'t', 't':'a', 'g':'c', 'c':'g'}

def compl(base):
    return bas_dict[base]

print(compl('a'))

def compl_string(string):
    comp_string=[]
    for element in string:
        comp_string.append(bas_dict[element])
    return ''.join(comp_string)

print(compl_string("aattccgtggc"))
# 1) Function that takes a string as a paratmeter and returns true if str contains at least 3 g false otherwise.

# def threeg(stri):
#     gsum = 0
#     for letter in stri.upper():
#         if letter == 'G':
#             gsum += 1
#     while gsum < 3:
#         return False

# print(threeg('ggg')

def g_count(any_str):
    gnum = 0 # need to count the g's
    for char in any_str.upper(): # char itterates through each char of the string .upper() ensures that no matter which string the format will be recognized.
        if char == 'G': # only if char is tha same as the string 'G'
            gnum += 1 # gnum increases by one.
    if gnum >= 3:   # this if must be BEHIND the firs if, so it only starts after first loop is completed.
        return True
    else:
        return False

print(g_count('attggg'))
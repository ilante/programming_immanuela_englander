#Exercise  1
list_1 = []
for i in range(3,16):
    list_1.append(i)

#Exercise 2
for x in list_1:
    if x%2 != 0: #tests for numbers in the list: if residual of number / 2 is 0, the number is even, otherwise it is odd.
        print(x)
print("\n")

#Exercise 3
for x in list_1:
    if x%5 == 0:
        print(x)
print("\n")

#Exercise 4, 5 and 6
list_2 = [5,2,7,8,1,-3]
print(list_2[0],list_2[2])
new_list2 = []
for i in list_2:
    new_list2.append(i*2)
print(new_list2)
print("\n")

#Exercise 7
list_2 = [5,2,7,8,1,-3]
new_list3 = []
for i in list_2:
    new_list3.append((i*2-2)/3)
print(new_list3)
print("\n")

#Exercise 8
x = 0
for i in new_list3:
    x += i
print(x)
print("\n")

#Exercise 9: print the minimum of the list
y = list_1
min = None
for i in y:
    if not min:
        min = i
    elif i < min:
        min = i
print (min)
print("\n")

#Exercise 10: print the maximum of the list
max = None
for i in y:
    if not max:
        max = i
    elif i > max:
        max = i
print(max)
print("\n")

#Exercise 11: Print the everage of a list
sum = 0
for i in y: 
    sum += i
average = sum / len(y)
print(average)
print("\n")

#Exercise 12
av = "avocado"
rad = "radar"
print("\n")

#Exercise 13
print (av[::-1], rad[::-1])
print("\n")

#Exercise 14: Evaluates if a sequence is a palindrome
x = av
y = rad
if x == x[::-1]:
    print(x, "is a palindrome")
else:
    print(x, "is not a palindrome")
print("\n")

#Exercise 15:
print(x[:len(x)//2])
print(y[len(y)//2:])
print("\n")

#Exercise 16: 
seq_1 = input("input template sequence:")
seq_2 = input("input test sequence:")
seq_1 = seq_1.upper()
seq_2 = seq_2.upper()

#Exercise 17, 18 & 22
def align (seq1,seq2):
    comp = ""
    i = 0
    non_comp=0
    for x in seq_2:
        if (x == "A" and seq_1[i] =="T") or (x == "T" and seq_1[i] == "A") or (x == "C" and seq_1[i] == "G") or (x == "G" and seq_1[i] == "C"):
            comp += "|"
        else:
            comp += "X"
            non_comp += 1
        i += 1
    return (seq_1+"\n"+comp+"\n"+seq_2+"\n"+"The number of non-complementary positions is: "+str(non_comp))
    
print(align(seq_1,seq_2))

#Another (more complicated but yet working) possible way to do it
def comp_bases(seq_1,seq_2):
    x=0
    seq_1_mod = ""
    for i in seq_1:  
        if (i=="A" or i == "T"):
            seq_1_mod += "1" 
        elif (i =="G" or i=="C"):
            seq_1_mod+= "2"
    seq_2_mod = ""
    for i in seq_2:   
        if (i=="A" or i == "T"):
            seq_2_mod += "1" 
        elif (i =="G" or i=="C"):
            seq_2_mod+= "2"
    con=""
    for i in seq_1_mod:
        if i == seq_2_mod[x]:
            con += "|"
        else:
            con += "X"
        x += 1
    return(seq_1 + "\n" + con + "\n" + seq_2)
print(comp_bases(seq_1,seq_2))
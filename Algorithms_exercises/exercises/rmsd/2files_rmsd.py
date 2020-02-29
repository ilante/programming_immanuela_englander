import math

file1 = 'm1.pdb'
file2 = 'm2.pdb'

#def rmsd(file1, file2)
inpdb = open('./'+ file1, 'r')
rpdb = inpdb.readline()
# print(inpdb.readline()) reads one line of the file

p=0
coordlist1 = []
for line in inpdb:
    list_model1 = line.split()
    if "CA" in list_model1 and list_model1[5] != p:
        p = list_model1[5]
        coordlist1.append(list_model1[6:9])
# print(len(coordlist1))

#def rmsd(file1, file2)
inpdb = open('./'+file2, 'r')
rpdb = inpdb.readline()
# print(inpdb.readline()) reads one line of the file
p=0
coordlist2 = []
for line in inpdb:
    list_model2 = line.split()
    if "CA" in list_model2 and list_model2[4] != p:
        p = list_model2[4]
        coordlist2.append(list_model2[5:8])
print(coordlist1)

print(len(coordlist1))

n=-1
m=-1
l=-1
o=-1
for coord in coordlist1:
    cord1 = coordlist1[n+1]
    cord2 = coordlist2[n+1]
    # print(cord1)


    for el in range(3):
        subcord1 = cord1[el]
        subcord2 = cord2[el]
        squared_element = (float(subcord1) - float(subcord2))**2
        sum_of_elements =0
        sum_of_elements = squared_element + sum_of_elements
# print(sum_of_elements)
print(math.sqrt((sum_of_elements)/len(coordlist2)))
    # num2=coordlist2[l+1][o+1]

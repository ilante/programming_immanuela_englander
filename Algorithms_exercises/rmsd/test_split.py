
#we test some splitting of liens in the PDB
#pdbfile = "./alignmentB0JDP9_1GYC.pdb"
pdbfile = "testfile.txt"

infile = open(pdbfile, "r")

# for line in infile:
# 	print("this is a line", line, end="")
# print('')

for line in infile:
	l=[]

	for e in line:
		if type(e) == int:
			l.append(e)	
print(x)

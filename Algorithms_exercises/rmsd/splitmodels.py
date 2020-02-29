# split file into 2 lists
# by variable.split("MODEL")
# n=1
# create list name+n
# start at word "MODEL      " 
# end at word "ENDMDL"
pdbfile = "./alignmentB0JDP9_1GYC.pdb"
opdb = open(pdbfile, "r")

def splitalign(inpfile):
    for line.startswith("ATOM" or "HETATM"):
        inpfile.split("MODEL")


for line in infile:
    if line.startswith("FN:"):
        names=line[3:].split()
        unders="_".join(names)
        gitfile.write("programming_"+unders.lower()+"\n")

# def rmsd(li1, li2):
#     for later hahaha

# TITLE     jCE V.1.1 : file:/home/ila/Downloads/1gyc.pdb vs.        
# TITLE    2 file:/home/ila/Downloads/B0JDP9.B99990002.pdb           
# EXPDTA    NMR, 2 STRUCTURES
# MODEL      1
# ATOM      1  N   ALA A   1      20.039 -10.070  25.413  1.00 31.50           N
# ATOM      2  CA  ALA A   1      20.656  -9.627  26.703  1.00 29.77           C
# ATOM      3  C   ALA A   1      22.138  -9.971  26.715  1.00 29.27           C
# ATOM      4  O   ALA A   1      22.577 -10.833  25.949  1.00 30.28           O
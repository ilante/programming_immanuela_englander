#Exercise 23
sequences = open("./10_sequences.txt","r") 
S1 = 0
S2 = 1
for x in sequences:
    x.rstrip()
    sequences.readline()
    print(x)
    #for i in x:
        #print(i)
        #c += 1
sequences.close()   
#print(str(c))

def makeDictionary(file,aminoacids):
    ''' Reads a substitution matrix from a text file and stores its values in a dictionary where the pairs of amino acids are the keys. The function returns the generated dictionary
    '''
    subsmat={}               # initializing empty dictionary
    for aminoacid in aminoacids:
        row=file.readline().split() # splits each line into a list
        for i in range(len(row)):
            couple=aminoacid+aminoacids[i]
            subsmat[couple]= float(row[i])           #add in the dictionary also the reverse couple
            subsmat[couple[::-1]]=float(row[i])      # as the matrix is symmetric
    return subsmat

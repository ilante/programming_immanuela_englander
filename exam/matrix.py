def multmatrix(matrix1,matrix2):
	matrix12=[]
	# Created an empty matrix to be filled later with the result of the product   
	for i in range(len(matrix1)): # range of 'colums' = len of the matrix (counting the sublists.
		row=[] #create sublist for rows 
		for j in range(len(matrix2[0])):
		       row.append(0)
		matrix12.append(row)
	#iterate through rows of matrix1
	#for i in range(len(matrix1)):
		#iterate through columns of matrix2
		for j in range(len(matrix2[0])):
		       #iterate through rows of matrix2
		       for k in range(len(matrix2)):
			       matrix12[i][j]+=matrix1[i][k]*matrix2[k][j]
	for r in matrix12:
	#pirnt the matrix resut of the product
		print (r)
	return matrix12

A = [[2,4],[3,1]]

B = [[2,1],[1,3]]

multmatrix(A, B)

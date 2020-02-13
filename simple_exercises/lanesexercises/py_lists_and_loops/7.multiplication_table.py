# # 7. print the multiplication table
# 10*10 matrix
first_row=[]
first_colum=[0]
for i in range(10): # first row from 1-10
    i += 1 #to start at index number 1 (not 0)
    first_row.append(i)
print(first_row)
for el in first_row[:len(first_row)-1]: #due to the i+1 it would end at 11...
        first_colum=[]
        first_colum.append(el+1)
        for el in first_colum, for i in first_row:
            el = el*(i+1)
        print(first_colum)
        # for j in range(len(first_colum):
        #     # print(j)
        #     first_colum.append(j*(j+1))
        #     print(first_colum)

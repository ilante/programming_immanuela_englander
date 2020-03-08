def blosum_from_txt(filehandle):
    bl45_dict = {}
    ma_list = []
    with open(filehandle, 'r') as o_file:
        for line in o_file:
            if line[0] != '#':
                ma_list.append(line.split())
    print(ma_list)
    for i in range(1, len(ma_list)):
        for j in range(1, len(ma_list)):
            print(ma_list[i][0]+ma_list[0][j], 'and ', int(ma_list[i][j]))
            bl45_dict[ma_list[i][0]+ma_list[0][j]] = int(ma_list[i][j])
    print(bl45_dict)
    return bl45_dict

bl = './blosum45.txt'

b45 = blosum_from_txt(bl)

# add to matrices.py
with open('./matrices.py', 'a') as a_file:
    a_file.write(str(b45))

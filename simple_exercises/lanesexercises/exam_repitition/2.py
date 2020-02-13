# Write a program that prints the third character of the first two lines of 'pippo.txt'. on the screen
infile = open("./pippo.txt", "r") 

for el in range(2):
    third_char=infile.readline()
    print(third_char[2])
infile.close()

print('another way to do it')
print('')

pip = open('./pippo.txt', 'r') # the result of open(... , 'r') is stored in pip
line1 = pip.readline()
line2 = pip.readline()
print(line1[2])
print(line2[2])

s='ana'
print(s[2])
y=s[2]
print(y)
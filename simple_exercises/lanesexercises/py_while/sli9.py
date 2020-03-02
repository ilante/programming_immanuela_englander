#    Write a code to the same effect of the one in previous slide, but without using break
line = ''
while line != 'done':
    line = input('>>')
    if line == 'done':
        print('bye')
    else: #line != 'done':
        print(line)
        # break   # stops the loop
    
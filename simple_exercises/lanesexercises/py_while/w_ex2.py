# 2. Use a while loop to compute the partial sums of a list of integers

# 3. Use a while loop to print all the characters of a string until you find two consecutive equal characters (which should not be printed). Is there any advantage of using a while loop instead of a for loop?

st = "Manamummi"
i = 0
two = st[i]+st[i+1]
while st[i] != st[i+1]:
    print(st[i], end='')
    i += 1
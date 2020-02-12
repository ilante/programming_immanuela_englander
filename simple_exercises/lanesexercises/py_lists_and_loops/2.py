# 2. extract the numbers from the string 
x='23|64|354|-123'
y=x.split("|")
print(y)
# same result as 
y='23|64|354|-123'.split('|')
print(y)

ana="Good Food and fun and chitter"
wurst=ana.split()
print(wurst)
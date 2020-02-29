print("4. Find the name of the youngest person")
ages = {'Peter': 52, 'Hannah': 19, 'Simone': 32, 'myself': 28}
k=''
youngest = 100000 # number higher than human age
for i in ages.keys():
    if ages[i] < youngest:
        youngest = ages[i]
        k = i
print(k)

# Thomas' take on it
Mydicq = {"James": 52, "Lauren": 22, "Neva": 24, "Thomas": 23}
young = max(Mydicq.values())
c = 0
for i in Mydicq.values():
    if i < young:
        young = i
        g = c
    else: 
         c = c + 1
a = list(Mydicq.keys())
LaurensAge = Mydicq["Lauren"]
print(LaurensAge)
print(a[g])

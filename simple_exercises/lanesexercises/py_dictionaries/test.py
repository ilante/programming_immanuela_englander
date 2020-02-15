lis = ["Ana", "Sahar", "Oscar", "Aya"]
lis_set = set(lis)
print(lis_set)

# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", "progressive rock", "soft rock", "R&B", "disco"])

print(music_genres)

# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
A.add("I really don't care about Michael Jackson")
print(A)

A.remove("Thriller")
print(A)

# Verify if the element is in the set

x="AC/DC" in A
print(x)

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

print(album_set1, album_set2)

y=album_set1 & album_set2
print(y)

# Use intersection method to find the intersection of album_list1 and album_list2

n=album_set1.intersection(album_set2)  
print(n)

b=album_set1.difference(album_set2)
print(b)

# Find the union of two sets
union= album_set1.union(album_set2)
print(union)

# Check if superset
supers = set(album_set1).issuperset(album_set2)  
print(supers)

# Check if subset
sub=set(album_set2).issubset(album_set1)
print(sub)

#Check if subset again.

again = set({'Back in Black', 'AC/DC'}).issubset(album_set1)

print(again)

for i,x in enumerate(['A','B','C']):
    print(i,2*x)
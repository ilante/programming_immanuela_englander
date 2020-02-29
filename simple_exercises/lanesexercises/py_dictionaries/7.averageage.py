print('7. Compute the average age')
ages = {'Peter': 52, 'Hannah': 19, 'Simone': 32, 'myself': 28}

# creating list of numbers from ages dictionary
numli = list(ages.values())

def average(li):
    sum = 0
    for num in li:
        sum += num
    return sum/len(li)

average_age = average(numli)
print(average_age)

# from statistics import mean  # to check if correct
# print(mean(numli)) 

number = input("Give me an integer! ")
summator = int(number)
while int(number) != 0:
    number = input("Give me an integer! ")
    summator += int(number)
print("The sum of the numbers inserted equals ",str(summator)+".")
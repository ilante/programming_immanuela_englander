li = [1, 42, 'spam']
len(li) #built in

def homemadeLEN(L):
    ''' returns the lenght of list L '''
    if L == []:
        return 0
    else:
        return 1 + homemadeLEN(L[1:])

print(homemadeLEN(li))
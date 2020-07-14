def ev_odd(st):
    odd = 0
    ev = 0
    for i in range(len(st)):
        if i%2 == 0 and st[i] == 'A':
            ev += 1
        elif i%2 != 0 and st[i] == 'A':
                odd += 1
    if odd == ev:
        return True
    return False


print(ev_odd('AAANANA'))
# https://www.coursera.org/lecture/principles-of-computing-2/recursion-ccrwD

# So for example, consider the problem of summing up all the numbers from n down to one. For all positive n. Okay, so I want to sum n plus n minus 1, plus n minus 2 and so on down to 1.

#example from the rice professor
def sum_n_down_to1(n):
    if n == 1:
        return 1
    else:
        return n + sum_n_down_to1(n-1)

# this works too
def sum_n_down_to1(n):
    if n == 1:
        return 1
    else:
        n = n + sum_n_down_to1(n-1)
        return n

print(sum_n_down_to1(5))


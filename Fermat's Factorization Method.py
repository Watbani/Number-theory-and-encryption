from math import ceil, sqrt

def Fermat_Factor(n):

    if (n <= 0):
        return
    if (n == 1):
        return [1]
    if (n & 1) == 0:
        return [Fermat_Factor(int(n / 2)), 2]

    x = ceil(sqrt(n))

    if (x * x == n):
        return [x, x]

    while (True):
        y1 = x * x - n
        y = int(sqrt(y1))
        Factor1 = x - y
        Factor2 = x + y
        if (y * y == y1):
            break
        else:
            x += 1
    if Factor1 > 1:
        for i in range(2, Factor1):
            if (Factor1 % i) == 0:
                return [Fermat_Factor(Factor1), Factor2]
        return [Factor1, Factor2]



print(Fermat_Factor(int(input("Enter the number you wish to factor: "))))
import numpy as np

def erato_sieve(num):
    allN = np.arange(1,num+1,1)
    mask = allN == allN
    maskN = np.ma.MaskedArray(allN)
    p = 2

    while maskN[p:].count() > 0:
        mask = mask & ((allN%p != 0) | (allN <= p))
        maskN = np.ma.MaskedArray(maskN, mask =~ mask)
        p = maskN[p:].min()

    return np.asarray(maskN[maskN.mask == False])

def factor(num):
    sieve = erato_sieve(num)
    flist = []
    num_factored = num
    for i in range(1, len(sieve)):
        while num_factored % sieve[i] == 0:
            flist.append(sieve[i])
            num_factored = num_factored // sieve[i]
            if num_factored == 1:
                break

    prime = len(flist) == 1

    if not prime:
        print("It's prime factors are:", flist)
    elif prime:
        print(flist, "is a prime number.")


num = int(input('Enter the number you wish to factor: '))
factor(num)

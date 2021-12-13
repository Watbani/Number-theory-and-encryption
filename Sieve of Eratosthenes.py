def sieve_of_era(num):
    priiiime = dict()
    numn = num+1
    for k in range(2, numn):
        priiiime[k] = True

    for k in priiiime:
        factors = range(k,numn, k)
        for v in factors[1:]:
            priiiime[v] = False
    return [k for k in priiiime if priiiime[k] == True]


print(sieve_of_era(int(input("Limit: "))))

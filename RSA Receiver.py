import random
import string

#import math
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def PickE(phiN):

    while (True):
        e = random.randrange(2, phiN)

        if (gcd(e, phiN) == 1):
            return e


p = int(input("p: "))
q = int(input("q: "))

n = p * q
phiN = (p - 1) * (q - 1)
e = PickE(phiN)

print("Your public key is:", "\n", "n:", n, "\n", "e:", e)

#we have generated the public key


def modInverse(e, phiN):
    for x in range(1, phiN):
        if (((e % phiN) * (x % phiN)) % phiN == 1):
            return x
    return -1
d = modInverse(e, phiN)
print("Your private key is:", d)

#we have generated the private key through the mod inverse

def decrypt(ct):
    decryption = int(ct) ** d
    decryption2 = decryption % n
    return decryption2
decrypt_input = input("Decrypt: ")

#the decryption function

decrypt_output = decrypt(decrypt_input)

print("Your Decrypted Message is:", decrypt_output)



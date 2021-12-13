
i = 1
j = input("How many times do you wish the encryptor to run? ")
while i <= int(j):
    i = i + 1
    dct1 = {'a': 'c', 'b': 'g', 'c':
    's', 'd': 'q', 'e': 'r', 'f':
        't', 'g': 'm', 'h': 'o', 'i': 'n', 'j': 'l', 'k': 'k', 'l': 'f', 'm': 'b',
            'n': 'a', 'o': 'e', 'p': 'x', 'q': 'y', 'r': 'z', 's': 'd', 't': 'p', 'u': 'w',
            'v': 'h', 'w': 'i', 'x': 'j', 'y': 'u', 'z': 'v', }


    def encrypt(text, dct=dct1):
        encrypted = []
        for i in text:
            encrypted.append(dct.get(i, i))
        encrypted = ''.join(encrypted)
        return encrypted


    encryption_message = input("Encrypt: ")
    print(encrypt(encryption_message))

    dct2 = {'c': 'a', 'g': 'b', 's': 'c', 'q': 'd', 'r': 'e', 't':
        'f', 'm': 'g', 'o': 'h', 'n': 'i', 'l': 'j', 'k': 'k', 'f': 'l', 'b': 'm',
            'a': 'n', 'e': 'o', 'x': 'p', 'y': 'q', 'z': 'r', 'd': 's', 'p': 't', 'w': 'u',
            'h': 'v', 'i': 'w', 'j': 'x', 'u': 'y', 'v': 'z', }


    def decrypt(text, dct=dct2):
        decrypted = []
        for i in text:
            decrypted.append(dct.get(i, i))
        decrypted = ''.join(decrypted)
        return decrypted


    decryption_message = input("Decrypt: ")
    print(decrypt(decryption_message))


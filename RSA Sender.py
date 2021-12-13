n = int(input("n: "))
e = int(input("e: "))

message = input("Encrypt: ")


#m ** e mod n
def encrypt(me):
    encryption = int(me) ** e
    encryption2 = encryption % n
    return encryption2

ct = encrypt(message)
print("Encrypted Message:", ct)










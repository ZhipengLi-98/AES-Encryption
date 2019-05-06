import AES

if __name__ == "__main__":
    key = 0x000102030405060708090a0b0c0d0e0f
    round = 10
    bits = 128
    msg = 0x75e651b3e55456a8e56e643c06371d2075e651b3e55456a8e56e643c06371
    ciph = 0x6ffc34aaff86389008a1cb22d0da94c7
    cryptor = AES.AES(key, round, bits)
    for i in cryptor.encrypt(msg):
        print(hex(i))
    for i in cryptor.decrypt(msg):
        print(hex(i))



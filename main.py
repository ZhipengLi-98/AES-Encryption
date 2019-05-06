import AES

if __name__ == "__main__":
    key = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
    round = 14
    bits = 256
    msg = "75e651b3e55456a8e56e643c06371d2075e651b3e55456a8e56e643c06371"
    ciph = "0c9af0650e41603a4995979a0241e70d901e01540d3c714216c58f5685ecc000"
    cryptor = AES.AES(key, round, bits)
    for i in cryptor.encrypt(msg):
        print(hex(i))
    for i in cryptor.decrypt(ciph):
        print(hex(i))



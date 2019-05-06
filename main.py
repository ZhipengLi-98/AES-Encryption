import AES

if __name__ == "__main__":
    key = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
    round = 14
    bits = 256
    cryptor = AES.AES(key, round, bits)
    print(hex(cryptor.encrypt(0xe54b04099c6c16ba14a0e25f4fb68dd4)))
    print(hex(cryptor.decrypt(0x6ffc34aaff86389008a1cb22d0da94c7)))

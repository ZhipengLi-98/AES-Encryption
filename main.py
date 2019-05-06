import AES

if __name__ == "__main__":
    key = 0x000102030405060708090a0b0c0d0e0f1011121314151617
    round = 12
    bits = 192
    cryptor = AES.AES(key, round, bits)
    print(hex(cryptor.encrypt(0xe54b04099c6c16ba14a0e25f4fb68dd4)))
    print(hex(cryptor.decrypt(0xa1d1d291adacd6dd4f272b267b520194)))

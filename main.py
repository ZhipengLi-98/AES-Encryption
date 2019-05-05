import AES

if __name__ == "__main__":
    cryptor = AES.AES(0x000102030405060708090a0b0c0d0e0f, 10)
    print(hex(cryptor.encrypt(0xe54b04099c6c16ba14a0e25f4fb68dd4)))

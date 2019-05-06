from Crypto.Cipher import AES

if __name__ == '__main__':
    t = AES.new(bytes.fromhex("000102030405060708090a0b0c0d0e0f"), AES.MODE_CBC, bytes.fromhex("00000000000000000000000000000000"))
    print((t.encrypt(bytes.fromhex("75e651b3e55456a8e56e643c06371d2075e651b3e55456a8e56e643c06371000"))).hex())
    print((t.decrypt(bytes.fromhex("75e651b3e55456a8e56e643c06371d2075e651b3e55456a8e56e643c06371000"))).hex())

'''
from example import AES


if __name__ == "__main__":
    test = AES(0x000102030405060708090a0b0c0d0e0f)
    print(hex(test.encrypt(0xe54b04099c6c16ba14a0e25f4fb68dd4)))
'''


from Crypto.Cipher import AES

if __name__ == '__main__':
    t = AES.new(bytes.fromhex("000102030405060708090a0b0c0d0e0f1011121314151617 "), AES.MODE_CBC, bytes.fromhex("00000000000000000000000000000000"))
    print((t.encrypt(bytes.fromhex("e54b04099c6c16ba14a0e25f4fb68dd4"))).hex())


'''
from test import AES


if __name__ == "__main__":
    test = AES(0x000102030405060708090a0b0c0d0e0f)
    print(hex(test.encrypt(0xe54b04099c6c16ba14a0e25f4fb68dd4)))
'''


from Crypto.Cipher import AES

if __name__ == '__main__':
    t = AES.new(bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c"), AES.MODE_CBC, bytes.fromhex("00000000000000000000000000000000"))
    print((t.encrypt(bytes.fromhex("3243f6a8885a308d313198a2e0370734"))).hex())


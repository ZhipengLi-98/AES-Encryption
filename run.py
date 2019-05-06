import AES
import time

if __name__ == "__main__":
    key = 0x000102030405060708090a0b0c0d0e0f
    round = 10
    bits = 128
    cryptor = AES.AES(key, round, bits)
    ans = []
    with open("16.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split("\n")[0]
            start = time.time()
            cryptor.encrypt(line)
            end = time.time()
            ans.append(str(end - start) + "\n")
    with open("16_128.txt", "w") as f:
        f.writelines(ans)
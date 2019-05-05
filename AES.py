from utils import *


class AES:
    def __init__(self, key, rounds):
        self.key = hex2mat(key)
        self.rounds = rounds
        self.extend_key(self.key)

    def extend_key(self, key):
        for i in range(4, 4 * (1 + self.rounds)):
            self.key.append([])
            if i % 4 == 0:
                temp = self.key[i - 4][0] ^ s_box[self.key[i - 1][1]] ^ r_con[int(i / 4)]
                self.key[i].append(temp)
                for j in range(1, 4):
                    temp = self.key[i - 4][j] ^ s_box[self.key[i - 1][(j + 1) % 4]]
                    self.key[i].append(temp)
            else:
                for j in range(4):
                    temp = self.key[i - 4][j] ^ self.key[i - 1][j]
                    self.key[i].append(temp)

    def round_add(self, state, keys):
        for i in range(4):
            for j in range(4):
                state[i][j] ^= keys[i][j]

    def sub_bytes(self, state):
        for i in range(4):
            for i in range(4):
                state[i][j] = s_box[s[i][j]]

    def encrypt(self, msg):
        state = hex2mat(msg)
        self.round_add(state, self.key[0: 4])
        for i in range(1, self.rounds):
            self.sub_bytes(state)
            self.shift_rows(state)
            self.mix_cols(state)
            self.round_add(state, self.key[4 * i: 4 * (i + 1)])

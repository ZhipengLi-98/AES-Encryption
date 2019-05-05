from utils import *


class AES:
    def __init__(self, key, rounds):
        self.key = hex2mat(key)
        self.rounds = rounds
        self.extend_key()

    def extend_key(self):
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
            for j in range(4):
                state[i][j] = s_box[state[i][j]]

    def shift_rows(self, state):
        state[0][1], state[1][1], state[2][1], state[3][1] = state[1][1], state[2][1], state[3][1], state[0][1]
        state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
        state[0][3], state[1][3], state[2][3], state[3][3] = state[3][3], state[0][3], state[1][3], state[2][3]

    def mix_cols(self, state):
        for i in range(4):
            temp = state[i][0] ^ state[i][1] ^ state[i][2] ^ state[i][3]
            backup = state[i][0]
            state[i][0] ^= temp ^ mult(state[i][0] ^ state[i][1])
            state[i][1] ^= temp ^ mult(state[i][1] ^ state[i][2])
            state[i][2] ^= temp ^ mult(state[i][2] ^ state[i][3])
            state[i][3] ^= temp ^ mult(state[i][3] ^ backup)

    def encrypt(self, msg):
        state = hex2mat(msg)
        self.round_add(state, self.key[0: 4])
        for i in range(1, self.rounds):
            self.sub_bytes(state)
            self.shift_rows(state)
            self.mix_cols(state)
            self.round_add(state, self.key[4 * i: 4 * (i + 1)])
        self.sub_bytes(state)
        self.shift_rows(state)
        self.round_add(state, self.key[4 * self.rounds: ])
        return mat2hex(state)

from utils import *


class AES:
    def __init__(self, key, rounds, bits):
        self.rounds = rounds
        self.bits = bits
        if bits == 128:
            self.key = hex2mat128(key)
            self.extend_key128()
        elif bits == 192:
            self.key = hex2mat192(key)
            self.extend_key192()
        elif bits == 256:
            self.key = hex2mat256(key)
            self.extend_key256()

    def extend_key128(self):
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

    def extend_key192(self):
        for i in range(6, 4 * (1 + self.rounds)):
            self.key.append([])
            if i % 6 == 0:
                temp = self.key[i - 6][0] ^ s_box[self.key[i - 1][1]] ^ r_con[int(i / 6)]
                self.key[i].append(temp)
                for j in range(1, 4):
                    temp = self.key[i - 6][j] ^ s_box[self.key[i - 1][(j + 1) % 4]]
                    self.key[i].append(temp)
            else:
                for j in range(4):
                    temp = self.key[i - 6][j] ^ self.key[i - 1][j]
                    self.key[i].append(temp)

    def extend_key256(self):
        print("extend_key256")

    def round_add(self, state, keys):
        for i in range(4):
            for j in range(4):
                state[i][j] ^= keys[i][j]

    def sub_bytes(self, state):
        for i in range(4):
            for j in range(4):
                state[i][j] = s_box[state[i][j]]

    def rev_sub_bytes(self, state):
        for i in range(4):
            for j in range(4):
                state[i][j] = rev_s_box[state[i][j]]

    def shift_rows(self, state):
        state[0][1], state[1][1], state[2][1], state[3][1] = state[1][1], state[2][1], state[3][1], state[0][1]
        state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
        state[0][3], state[1][3], state[2][3], state[3][3] = state[3][3], state[0][3], state[1][3], state[2][3]

    def rev_shift_rows(self, state):
        state[0][1], state[1][1], state[2][1], state[3][1] = state[3][1], state[0][1], state[1][1], state[2][1]
        state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
        state[0][3], state[1][3], state[2][3], state[3][3] = state[1][3], state[2][3], state[3][3], state[0][3]

    def mix_cols(self, state):
        for i in range(4):
            temp = state[i][0] ^ state[i][1] ^ state[i][2] ^ state[i][3]
            backup = state[i][0]
            state[i][0] ^= temp ^ mult(state[i][0] ^ state[i][1])
            state[i][1] ^= temp ^ mult(state[i][1] ^ state[i][2])
            state[i][2] ^= temp ^ mult(state[i][2] ^ state[i][3])
            state[i][3] ^= temp ^ mult(state[i][3] ^ backup)

    def rev_mix_cols(self, state):
        for i in range(4):
            tempa = mult(mult(state[i][0] ^ state[i][2]))
            tempb = mult(mult(state[i][1] ^ state[i][3]))
            state[i][0] ^= tempa
            state[i][1] ^= tempb
            state[i][2] ^= tempa
            state[i][3] ^= tempb
        self.mix_cols(state)

    def encrypt(self, msg):
        state = hex2mat128(msg)
        self.round_add(state, self.key[0: 4])
        for i in range(1, self.rounds):
            self.sub_bytes(state)
            self.shift_rows(state)
            self.mix_cols(state)
            self.round_add(state, self.key[4 * i: 4 * (i + 1)])
        self.sub_bytes(state)
        self.shift_rows(state)
        self.round_add(state, self.key[4 * self.rounds: ])
        return mat2hex128(state)

    def decrypt(self, msg):
        state = hex2mat128(msg)
        self.round_add(state, self.key[4 * self.rounds: ])
        for i in range(self.rounds - 1, 0, -1):
            self.rev_shift_rows(state)
            self.rev_sub_bytes(state)
            self.round_add(state, self.key[4 * i: 4 * (i + 1)])
            self.rev_mix_cols(state)
        self.rev_shift_rows(state)
        self.rev_sub_bytes(state)
        self.round_add(state, self.key[ :4])
        return mat2hex128(state)

class AES:
    def __init__(self):
        # Initial Value for ECB AES-128
        # s-box for encryption
        self.s_box = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
                      0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
                      0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
                      0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
                      0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
                      0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
                      0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
                      0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
                      0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
                      0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
                      0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
                      0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
                      0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
                      0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
                      0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
                      0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
                      0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
                      0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
                      0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
                      0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
                      0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
                      0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
                      0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
                      0x54, 0xbb, 0x16]

        # s-box for decryption bcz we use ebc
        self.inv_s_box = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
                          0x9e, 0x81, 0xf3, 0xd7, 0xfb, 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f,
                          0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb, 0x54,
                          0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b,
                          0x42, 0xfa, 0xc3, 0x4e, 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24,
                          0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25, 0x72, 0xf8,
                          0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,
                          0x65, 0xb6, 0x92, 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
                          0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84, 0x90, 0xd8, 0xab,
                          0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3,
                          0x45, 0x06, 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1,
                          0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b, 0x3a, 0x91, 0x11, 0x41,
                          0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6,
                          0x73, 0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9,
                          0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e, 0x47, 0xf1, 0x1a, 0x71, 0x1d,
                          0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
                          0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
                          0xfe, 0x78, 0xcd, 0x5a, 0xf4, 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
                          0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f, 0x60,
                          0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f,
                          0x93, 0xc9, 0x9c, 0xef, 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5,
                          0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61, 0x17, 0x2b,
                          0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55,
                          0x21, 0x0c, 0x7d]

        # column for matrix operation
        self.column_num = 4
        # key size for key expansion in AES-128
        self.key_size = 16
        # round for AES-128
        self.round_num = 10

        # Constant for Round in Key Expansion
        self.r_con = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

    # Encryption gogogo
    def encrypt(self, data, key):
        # Init block data
        datablock = bytearray(16)
        resultblock = bytearray(16)

        # get the expanded key key scheduler
        expanded_key = self.key_scheduler(key)

        # turn original data into datablock with 16 length
        for i in range(self.column_num):
            for j in range(self.column_num):
                datablock[(i + (j * self.column_num))] = data[(i * self.column_num) + j]

        # round 0
        # Add round-key for datablock with key-pointer 0
        initpointer = 0
        datablock = self.add_round(datablock, expanded_key, initpointer)

        # round 1-9
        # Substitute-ShiftRow-MixColumn-AddRound
        for i in (range(1, self.round_num)):
            datablock = self.sub_bytes(datablock)
            datablock = self.shift_row(datablock)
            datablock = self.mix_column(datablock)
            datablock = self.add_round(datablock, expanded_key, 16 * i)

        # final round
        # Substitute and Shift
        # Add round-key for datablock with key-pointer 10
        datablock = self.sub_bytes(datablock)
        datablock = self.shift_row(datablock)
        x = (16 * self.round_num)
        datablock = self.add_round(datablock, expanded_key, x)

        # fill resultblock with datablock recoded back into data original format
        for k in range(4):
            for l in range(4):
                resultblock[(k * 4) + l] = datablock[(k + (l * 4))]

        # return the result as an bytes
        finaldata = bytes(resultblock)
        return finaldata

    # Decryption gogogo
    def decrypt(self, data, key):
        # Init block data
        datablock = bytearray(16)
        resultblock = bytearray(16)

        # get the expanded key key scheduler
        expanded_key = self.key_scheduler(key)

        # turn original data into datablock with 16 length
        for i in range(self.column_num):
            for j in range(self.column_num):
                datablock[(i + (j * self.column_num))] = data[(i * self.column_num) + j]

        # round 10
        # Add round-key for datablock with key-pointer 10
        initpointer = self.round_num
        datablock = self.add_round(datablock, expanded_key, initpointer)

        # round 9-1
        # ShiftRow-Substitute-AddRound-MixColumn
        for i in (range(self.round_num - 1, 0, -1)):
            datablock = self.inv_shift_row(datablock)
            datablock = self.inv_sub_bytes(datablock)
            datablock = self.add_round(datablock, expanded_key, 16 * i)
            # Three times mixcolumn equals to Inverse Matrix => M X M X M = M^-1
            datablock = self.mix_column(datablock)
            datablock = self.mix_column(datablock)
            datablock = self.mix_column(datablock)

        # final round
        # Substitute and Shift
        # Add round-key for datablock with key-pointer 0
        datablock = self.inv_sub_bytes(datablock)
        datablock = self.inv_shift_row(datablock)
        x = 0
        datablock = self.add_round(datablock, expanded_key, x)

        # fill resultblock with datablock recoded back into data original format
        for k in range(4):
            for l in range(4):
                resultblock[(k * 4) + l] = datablock[(k + (l * 4))]

        # return the result as an bytes
        finaldata = bytes(resultblock)
        return finaldata

    def key_scheduler(self, key):
        # expansion key size with n+1 round size
        key_expanded_size = (self.round_num+1)*self.key_size
        key_size_loop = self.key_size
        # fill the init round with the key itself
        expanded_key = bytearray(key_expanded_size)
        expanded_key[:len(key)] = key
        # Set the round for later
        round = 1

        while key_size_loop < key_expanded_size:
            # Get the previous Round Key
            prev_key = expanded_key[key_size_loop - self.column_num:key_size_loop]  # 1

            # rotate word so a,b,c,d => b,c,d,a
            rotated_key = prev_key[1:] + prev_key[:1]
            # substitute again from SBox
            listrotate = [self.s_box[i] for i in rotated_key]
            rotated_key = bytearray(listrotate)
            # xor current byte with round constant based on current round
            rotated_key[0] = rotated_key[0] ^ self.r_con[round]

            # Do xor for each 4 bytes in a round except for first bytes with additional constant round
            for i in range(4):
                if i > 0:
                    rotated_key = expanded_key[key_size_loop - 4:key_size_loop]
                listkey = [i ^ j for i, j in zip(expanded_key[
                                                 key_size_loop - self.key_size:key_size_loop - self.key_size + self.column_num],
                                                 rotated_key)]
                resultkey = bytearray(listkey)
                expanded_key[key_size_loop:key_size_loop + self.key_size] = resultkey
                key_size_loop += 4

            # Go to next round
            round += 1
        # Trim the key
        return expanded_key[:key_expanded_size]

    # Add Round Key for Encyrption/Decryption
    def add_round(self, currentblock, expanded_key, keypointer):
        # xor the block with the round key using Generator and Bytearray
        round_key = bytearray(16)
        for i in range(self.column_num):
            for j in range(self.column_num):
                round_key[j * self.column_num + i] = expanded_key[keypointer + i * self.column_num + j]
        listkey = [i ^ j for i, j in zip(currentblock, round_key)]
        resultkey = bytearray(listkey)
        return resultkey

    # Substitute Bytes for Encyrption
    def sub_bytes(self, currentblock):
        listblock = [self.s_box[i] for i in currentblock]
        resultblock = bytearray(listblock)
        return resultblock

    # Substitute Bytes for Decryption
    def inv_sub_bytes(self, currentblock):
        listblock = [self.inv_s_box[i] for i in currentblock]
        resultblock = bytearray(listblock)
        return resultblock

    # Shifting Row for Encyrption
    def shift_row(self, currentblock):
        # Turn the block into 2d Matrix
        matrix = [bytearray(self.column_num) for i in range(self.column_num)]
        for i in range(self.column_num):
            for j in range(self.column_num):
                matrix[i][j] = currentblock[(i * self.column_num) + j]

        # a,b,c,d => b,c,d + a
        matrix[1] = matrix[1][1:] + matrix[1][:1]
        # a,b,c,d => c,d + a,b
        matrix[2] = matrix[2][2:] + matrix[2][:2]
        # a,b,c,d => d + a,b,c
        matrix[3] = matrix[3][3:] + matrix[3][:3]

        currentblock = bytearray(16)
        # Reverse into the datablock format from 2d Matrix
        for i in range(self.column_num):
            for j in range(self.column_num):
                currentblock[(i + (j * self.column_num))] = matrix[j][i]

        return currentblock

    # Shifting Row for Decryption
    def inv_shift_row(self, currentblock):
        # Turn the block into 2d Matrix
        matrix = [bytearray(self.column_num) for i in range(self.column_num)]
        for i in range(self.column_num):
            for j in range(self.column_num):
                matrix[i][j] = currentblock[(i * self.column_num) + j]

        # b,c,d,a => a + b,c,d
        matrix[1] = matrix[1][-1:] + matrix[1][:-1]
        # c,d,a,b => a,b + c,d
        matrix[2] = matrix[2][-2:] + matrix[2][:-2]
        # d,a,b,c => a,b c + d
        matrix[3] = matrix[3][-3:] + matrix[3][:-3]

        currentblock = bytearray(16)
        # Reverse into the datablock format from 2d Matrix
        for i in range(self.column_num):
            for j in range(self.column_num):
                currentblock[(i + (j * self.column_num))] = matrix[j][i]

        return currentblock

    # Mix Column Requirement
    # Multiplying by 2 is what your question is about: it is equivalent to shifting the number left by one, and then exclusiving-or'ing the value 0x1B if the high bit had been one
    def multiply_by_2(self, value):
        s = value << 1
        s &= 0xff
        if (value & 128) != 0:
            s = s ^ 0x1b
        return s

    # Mix Column Requirement
    # 3×x=(2⊕1)×x=(2×x)⊕x
    def multiply_by_3(self, value):
        v = self.multiply_by_2(value) ^ value
        return v

    # Mix Column for Encyrption/Decryption
    def mix_column(self, currentblock):
        for i in range(self.column_num):
            # process by each column with interval 4(self.column_num)
            # 0,4,8,12 , 1,5,9,13, etc
            column = currentblock[i:i + 16:self.column_num]
            # use multiply based on matrix
            # 2 3 1 1
            # 1 2 3 1
            # 1 1 2 3
            # 3 1 1 2
            listcollumn = [i for i in column]
            c = bytearray(listcollumn)
            column[0] = self.multiply_by_2(c[0]) ^ self.multiply_by_3(c[1]) ^ c[2] ^ c[3]
            column[1] = c[0] ^ self.multiply_by_2(c[1]) ^ self.multiply_by_3(c[2]) ^ c[3]
            column[2] = c[0] ^ c[1] ^ self.multiply_by_2(c[2]) ^ self.multiply_by_3(c[3])
            column[3] = self.multiply_by_3(c[0]) ^ c[1] ^ c[2] ^ self.multiply_by_2(c[3])
            currentblock[i:i + 16:4] = column
        # return the value of mixed block
        return currentblock
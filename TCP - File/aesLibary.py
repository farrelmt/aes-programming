from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 16  # Bytes
key = b'lorem ipsum dolo'

class AESLibary:
    def __init__(self):
        pass

    def dataEncrypt(data):
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(data, BLOCK_SIZE))
        return ciphertext

    def dataDecrypt(data, key):
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = cipher.decrypt(data)
        return unpad(plaintext, BLOCK_SIZE)

    # arg = input('Enter a message : ')
    # arg = bytes(arg, 'utf-8')
    # ciphertext = dataEncrypt(arg)
    # plaintext = dataDecrypt(ciphertext)
    # print(arg)
    # print(f'Cipher Text : {ciphertext}')
    # print(f'Plain Text : {plaintext}')

    ###
    # file = open('File/file1.txt', "rb")
    # if not file:
    #     print("NO FILE")
    # filea = file.read()
    # print("file")
    # data = dataEncrypt(filea)
    # data2 = dataDecrypt(data)
    # file2 = open('File/file1.txt', "wb+")
    # file2.write(data2)
    # filea.close()
    # file2.close()
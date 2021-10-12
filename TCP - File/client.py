import socket
import sys
from aesLibary import AESLibary
from aes_libary import AES

aes = AES()
PORT = 5000
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
FILEDIR = "File/"
FILENAME = ""
MODE_ENCRYPTION = ""


def main():
    # Take Argument
    FILENAME = sys.argv[1]
    MODE_ENCRYPTION = sys.argv[2]

    # START TCP SOCKET CLIENT
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # CONNECT TO SERVER
    client.connect(ADDR)

    # OPEN DAN READ FILE DATA
    file = open(FILEDIR + FILENAME, "rb")

    # SEND FILENAME TO SERVER
    client.send(FILENAME.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"{msg}")

    # SEND FILE DATA TO SERVER
    while True:
        data_bytes = file.read()
        if not data_bytes:
            # if transmiting done
            break

        if int(MODE_ENCRYPTION) == 1:
            withLibary(client, data_bytes)

        elif int(MODE_ENCRYPTION) == 2:
            withoutLibary(client, data_bytes)

        else:
            print("Choose Method Encryption")


    print("FILE RECEIVED")

    # CLOSE FILE
    file.close()

    # DISCONNECT FROM SERVER
    client.close()

def withoutLibary(client, data_bytes):
    data_enc = aes.encrypt_ecb(data_bytes,b'lorem ipsum dolo')
    client.sendall(data_enc)


def withLibary(client, data_bytes):
    data_enc = AESLibary.dataEncrypt(data_bytes)
    client.sendall(data_enc)

if __name__ == "__main__":
    main()

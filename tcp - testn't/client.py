import socket

PORT = 5000
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
FILENAME = "File/photo1.jpg"


def main():
    # START TCP SOCKET CLIENT
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # CONNECT TO SERVER
    client.connect(ADDR)

    # OPEN DAN READ FILE DATA
    file = open(FILENAME, "rb")

    # SEND FILENAME TO SERVER
    client.send("photo1.jpg".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"{msg}")

    # SEND FILE DATA TO SERVER
    while True:
        k_bytes = file.read(SIZE)
        if not k_bytes:
            # if transmiting done
            break
        client.sendall(k_bytes)

    print("FILE RECEIVED")

    # CLOSE FILE
    file.close()

    # DISCONNECT FROM SERVER
    client.close()


if __name__ == "__main__":
    main()

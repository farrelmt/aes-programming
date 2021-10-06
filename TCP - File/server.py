import socket

PORT = 5000
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


def main():
    # START TCP SOCKET SERVER
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # REUSE SERVER AFTER CLOSING
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # BIND IP & PORT to SERVER
    server.bind(ADDR)

    print("START SERVER")

    # Server is  waiting for the client to connected
    server.listen()
    print("SERVER IS LISTENING")

    while True:
        # Server accepted the connection from the client
        conn, addr = server.accept()
        print(f"{addr} CONNECTED")

        # Server Receiving the filename from the client
        filename = conn.recv(SIZE).decode(FORMAT)
        print("RECEIVING FILE NAME")
        file = open(filename, "wb+")
        conn.send("REQUEST RECEIVED".encode(FORMAT))

        # Receiving the file data from the client
        print("SENDING FILE...")
        while True:
            data = conn.recv(SIZE)
            if not data:
                # if nothing received
                break
            file.write(data)

        # Closing the file
        file.close()

        # Closing the connection from the client
        conn.close()
        print(f"{addr} DISCONNECTED.")

        # Close Server
        closeServer(server)


def closeServer(server):
    server.shutdown(socket.SHUT_RDWR)
    server.close()
    print("SERVER CLOSED")
    pass


if __name__ == "__main__":
    main()

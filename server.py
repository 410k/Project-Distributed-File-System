import socket


def create_socket():
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    port = 9999

    # bind to the port
    serversocket.bind((host, port))

    return serversocket


def main():

    # establish a connection
    serversocket = create_socket()

    # queue up to 5 requests
    serversocket.listen(5)

    while True:

        clientsocket, addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))

        msg = "Thank you for connecting"
        clientsocket.send(msg.encode("utf-8"))

        while True:

            msg = clientsocket.recv(1024)
            if msg.decode("utf-8") == "close":
                clientsocket.close()
            else:
                if msg.decode("utf-8") == "download":
                    msg = "Here is your downloaded file haha"
                    clientsocket.send(msg.encode("utf-8"))
                else:
                    clientsocket.send(msg)


main()

#!/usr/bin/python3

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1234))

# Max of 5 clients

mySocket.listen(5)

odd = True

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        peticion = recvSocket.recv(2048).decode("utf-8", "strict")
        recurso = peticion.split()[1][1:]
        if recurso == "favicon.ico":
            print("entra if")
            recvSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n" +
                            "<html><body><h1>Not Found!</h1>" +
                            "</body></html>" + "\r\n", 'utf-8'))
            recvSocket.close()
            continue
        if odd:
            
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>Me has enviado un :</h1>" +
                            "<p>" + recurso + "</p>" +
                            "</body></html>" + "\r\n", 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()

import socket

clnt_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

while True:
    clnt_sock.connect(('localhost', 9190))

    clnt_sock.send("Hello")

    data = clnt_sock.recv(1024)

    print('Message from server : ', data)


clnt_sock.close()
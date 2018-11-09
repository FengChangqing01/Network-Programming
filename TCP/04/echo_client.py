import socket

clnt_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
clnt_sock.connect(('localhost', 9190))
print("Connecting....")

while True:
    message = input('Input message(Q to quite): ')
    if message == 'Q':
        break

    clnt_sock.send(message)
    data = clnt_sock.recv(1024)
    print('Message from server : ', data)

clnt_sock.close()
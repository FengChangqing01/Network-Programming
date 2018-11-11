import socket

clnt_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
clnt_sock.connect(('localhost', 9190))
print("Connecting....")

while True:
    message = input('Input message(Q to quite): ')
    if message == 'Q':
        break
    clnt_sock.sendall(message.encode('ascii'))

    data = b''
    while len(data) < len(message):
        more = clnt_sock.recv(len(message)-len(data))
        data += more
    print('Message from server : ', data)
clnt_sock.close()
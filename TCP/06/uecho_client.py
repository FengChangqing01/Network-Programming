import socket

clent_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clent_sock.connect(('localhost', 9190))

while True:
    message = input('Input meaasge: ')
    if message == 'Q':
        break
    # clent_sock.sendto(message.encode('ascii'), ('localhost', 9190))
    clent_sock.sendall(message.encode('ascii'))
    data = clent_sock.recv(1024)
    print('Message form server : ', data)
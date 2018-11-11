import socket

clent_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input('Input meaasge: ')
    if message == 'Q':
        break
    clent_sock.sendto(message.encode('ascii'), ('localhost', 9190))
    data = clent_sock.recv(1024)
    print('Message form server : ', data)
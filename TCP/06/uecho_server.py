import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 9190))

while True:
    data, clent_addr = sock.recvfrom(1024)
    print('client from : ',clent_addr)
    sock.sendto(data, clent_addr)

sock.close()
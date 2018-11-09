import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

server_socket.bind(('localhost', 9190))

server_socket.listen(5)

for i in range(5):
    client_socket , client_socket_addr = server_socket.accept()
    print('client from '+str(client_socket_addr))
    if not (data = client_socket.recv(1024)):
        print('messages is '+str(data))
    client_socket.send(data)
    client_socket.close()

server_socket.close()
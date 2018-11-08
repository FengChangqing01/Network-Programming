import socket

message = b"Hello World"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 9200))

server.listen(10)

print("listenning at: "+ str(server.getsockname()))

sc, address = server.accept()

print("client from "+ str(address))

sc.sendall(message)
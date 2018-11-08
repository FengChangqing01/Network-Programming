import socket

message1 = b"Hello World"
message2 = b"HaHaHa"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

server.bind(("127.0.0.1", 9200))

server.listen(10)

print("listenning at: "+ str(server.getsockname()))

sc, address = server.accept()

print("client from "+ str(address))

sc.send(message1)

sc.send(message2)
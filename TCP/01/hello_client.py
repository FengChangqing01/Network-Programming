import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 9200))

print("client at :" + str(client.getsockname()))

message = client.recv(200)

message = ''
while True:
    data = client.recv(1)
    if not data:
        break
    message += str(data)

print(message)

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 9200))

print("client at :" + str(client.getsockname()))

meaasge = client.recv(20)

print(meaasge)
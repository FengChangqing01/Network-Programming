import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost',9190))

num_opt = input("Operand count: ")
num_opt = int(num_opt)

for i in range(1, num_opt+1):
    ope = input("Operand "+str(i))
    ope = int(ope)
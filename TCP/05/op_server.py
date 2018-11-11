import socket
import math

seve_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
seve_sock.bind(('localhost', 9190))
seve_sock.listen(5)
print("listenning ......")

while True:
    clent_sock, clent_sock_addr = seve_sock.accept()
    print("client from : ", clent_sock_addr)
    num_opt = clent_sock.recv(1)

    n = 0
    opt_number = []
    while n < num_opt:
        opt_number[n] = clent_sock.recv(1)
        n += 1
    
    opt_act = clent_sock.recv(1)

    answer = 0
    if opt_act == '+':
        for i in opt_number:
            answer += i
    elif opt_act == '-':
        for i in opt_number:
            answer -= i
    elif opt_act == '*':
        for i in opt_number:
            answer *= i
    
    clent_sock.sendall(answer)
    clent_sock.close()

seve_sock.close()
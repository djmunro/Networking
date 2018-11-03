import socket
import time

host = '127.0.0.1'
port = 5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

still_running = True

print('Server started.')

while still_running:
    try:
        data, addr = s.recvfrom(1024)
        if 'Quit' in str(data):
            still_running = False
        if addr not in clients:
            clients.append(addr)
        
        print(time.ctime(time.time()) + str(addr) + ': :' + str(data))
        for client in clients:
            s.sendto(data, client)
    except:
        pass

s.close()

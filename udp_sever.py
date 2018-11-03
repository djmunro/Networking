import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.bind((host, port))

    print('Server started.')
    while True:
        data, addr = s.recvfrom(1024)
        print('message from: {}' + str(addr))
        print('from connected user: ' + str(data))
        data = str(data).upper()
        print('Sending: ' + data)
        s.sendto(data, addr)
    s.close()

if __name__ == '__main__':
    main()
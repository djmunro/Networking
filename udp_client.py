import socket

def main():
    host = '127.0.0.1'
    port = 5001

    server = ('127.0.0.1', 5000)

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.bind((host, port))

    message = raw_input('-> ')
    while message != 'q':
        s.sendto(message, server)
        data, addr = s.recvfrom(1024)
        print('Recieved from server: ' + str(data))
        message = raw_input('-> ')
    s.close()

if __name__ == '__main__':
    main()

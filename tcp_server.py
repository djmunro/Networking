import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print('Connection from: {}'.format(str(addr)))

    while True:
        data = c.recv(1024)
        if not data:
            break
        print('from connected user: {}'.format(str(data)))
        data = str(data).upper()
        print('sending: {}'.format(str(data)))
        c.send(data)
    c.close()

if __name__ == '__main__':
    main()
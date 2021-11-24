import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as all:
    all.bind(('0.0.0.0', 50007))
    while True:
        recvdata, fromaddr = all.recvfrom(1024)
        print('data: {}, addr: {}'.format(recvdata, fromaddr))
        
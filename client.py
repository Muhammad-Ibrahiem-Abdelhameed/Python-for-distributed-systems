import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345

s.connect(('127.0.0.1', port))


while True:
    message = input('message you need \n')

    s.send(message.encode('ascii'))

    data = s.recv(1024)

    print("Received", str(data))
    ans = input('continue [y,n]')

    if ans == 'y':
        continue
    else:
        break

s.close()

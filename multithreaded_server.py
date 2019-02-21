import socket
#from socket import *
import threading
from _thread import *
print_lock = threading.Lock()

def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print_lock.acquire()
            print('bye')
            print_lock.release()
            break

        data = data[::-1]
        c.send(data)

    c.close()

def main():
    host = ""
    port =12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print('sock is lise')

    while True:
        c, addr = s.accept()

        print_lock.acquire()
        print('connect : ', addr[0], ':', addr[1])
        print_lock.release()

        start_new_thread(threaded, (c,))

    s.close()

main()
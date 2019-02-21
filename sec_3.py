import time
import threading

x = 0
def add():
    global x
    for i in range(1000000) :
        x += 1


def subtract():
    global x
    for i in range(1000000):
        x -= 1

a = threading.Thread(target=add)
s = threading.Thread(target=subtract)

a.start()
s.start()
a.join()
s.join()
print(x)
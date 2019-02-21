import time
import threading


x = 0
x_lock = threading.Lock()


def add():
    global x
    for i in range(1000000) :
        x_lock.acquire()
        x += 1
        x_lock.release()


def subtract():
    global x
    for i in range(1000000):
        x_lock.acquire()
        x -= 1
        x_lock.release()

a = threading.Thread(target=add)
s = threading.Thread(target=subtract)

startTime = time.time()
a.start()
a.join()
s.start()
s.join()
print(time.time()-startTime)
print(x)
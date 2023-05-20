# Q: Can threads change variables in the main process?
# A: Yes


from threading import Thread
from time import sleep


e = Exception()
x = 1


def f():
    e.a = 1
    global x
    x += 1
    sleep(0.5)


t = Thread(target=f)
t.start()
sleep(0.1)
print(e.a, x)
t.join()
print(e.a, x)

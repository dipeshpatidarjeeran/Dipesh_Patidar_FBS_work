from threading import Thread
import time

def fun1(str):
    for i in str:
        print(i, end=' ')
        time.sleep(1)

def fun2(str):
    for i in str:
        print(i, end=' ')
        time.sleep(1)

t1 = Thread(name="thread1",target=fun1, args=("11111111111111",))
t2 = Thread(name="thread2",target=fun2, args=("22222222222222",))
t1.start()
t2.start()
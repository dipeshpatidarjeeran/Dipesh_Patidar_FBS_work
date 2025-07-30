from threading import Thread
import time

def fun1(str):
    with open("corePython/Demos/MultitreadingEx/ex1.py", 'a') as fp:
        for i in str:
            fp.write(i)
            time.sleep(1)

def fun2(str):
    with open("corePython/Demos/MultitreadingEx/ex2.py", 'a') as fp:
        for i in str:
            fp.write(i)
            time.sleep(1)

t1 = Thread(name="Thread1", target=fun1, args=("111111111111",))
t2 = Thread(name="Thread2", target=fun2, args=("222222222222",))
t1.start()
t1.join(5)
t2.start()
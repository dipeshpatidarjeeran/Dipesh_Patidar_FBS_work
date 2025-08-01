from threading import Thread
import time

def withdrow(amt):
    with open("corePython/Demos/MultitreadingEx/balance.txt", "r") as fp:
        bal = int(fp.read())
        bal -= amt
    with open("corePython/Demos/MultitreadingEx/balance.txt", "w") as fp:
        fp.write(str(bal))
        print("withdrow bal:",bal)

def deposite(amt):
    with open("corePython/Demos/MultitreadingEx/balance.txt", "r") as fp:
        bal = int(fp.read())
        bal += amt

    with open("corePython/Demos/MultitreadingEx/balance.txt", "w") as fp:
        fp.write(str(bal))
        print("deposite bal:",bal)


t1 = Thread(name="thread1", target=deposite, args=(2000,))
t2 = Thread(name="thread2", target=withdrow, args=(3000,))
t1.start()
t2.start()
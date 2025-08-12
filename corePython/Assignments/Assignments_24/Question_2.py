# Create two threads, one printing even numbers and the other printing odd numbers
# from 1 to 10. Ensure proper synchronization to alternate between even and odd
# numbers.
from threading import Thread, Condition

condition = Condition()

def even(start,end):
    for i in range(start,end+1):
        with condition:
            if i%2 ==0:
                print(i, end=' ')
                condition.notify_all()
            else:
                condition.wait()

def odd(start, end):
    for i in range(start,end+1):
        with condition:
            if i%2 != 0:
                print(i,end=' ')
                condition.notify_all()
            else:
                condition.wait()

t1 = Thread(name="thread1", target=even, args=(1,10))
t2 = Thread(name="thread2", target=odd, args=(1,10))

t1.start()
t2.start()
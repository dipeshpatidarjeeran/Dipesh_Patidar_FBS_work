# Calculate the sum of squares of numbers from 1 to 100 using four threads. Divide the
# range equally among the threads, and each thread calculates the sum of squares for its
# range. Finally, combine the results to get the total sum of squares.
from threading import Thread
li = []
def sum_of_squares(a,b):
    add = 0
    for i in range(a,b+1):
        add += i**2
    li.append(add)



t1 = Thread(name="thread1", target=sum_of_squares, args=(1,25))
t2 = Thread(name="thread2", target=sum_of_squares, args=(26,50))
t3 = Thread(name="thread3", target=sum_of_squares, args=(51,75))
t4 = Thread(name="thread4", target=sum_of_squares, args=(76,100))
t1.start()
t2.start()
t3.start()
t4.start()


print(sum(li))
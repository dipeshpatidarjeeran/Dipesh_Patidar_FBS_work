# 1. We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def fibo(n):
    a = -1
    b = 1
    c = 0
    while(c <= n):
        c = a + b
        a = b
        b = c
        if c <= n:
            yield c 

n = int(input("how many print fibonacci series you want:-"))
f = fibo(n)
for i in f:
    print(i)
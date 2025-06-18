"""
    Write a program to find print the following Fibonacci series using
    functions:
    1 1 2 3 5 8 n terms
"""
def fibonacci(n):
    a=-1
    b = 1
    for i in range(1,n+1):
        c = a+b
        a = b
        b = c
        print(c, end=' ')

n = int(input("enter the number of series:-"))
fibonacci(n)
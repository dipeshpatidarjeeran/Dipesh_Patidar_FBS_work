"""
    Write a program to print Fibonacci series upto n.
"""
n = int(input("enter the number:-"))
a = 0
b = 1
for i in range (0,n):
    fib = a
    print(fib)
    a=a+b
    b=fib
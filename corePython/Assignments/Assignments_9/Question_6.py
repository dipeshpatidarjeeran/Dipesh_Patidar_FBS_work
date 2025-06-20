"""
    Write a program to print Fibonacci series using recursion.
"""
def fibonacci(n,a,b):
    if n==0:
        return 
    else:
        c = a+b
        print(c,end=' ')
        a=b
        b=c
        return fibonacci((n-1),a,b)
    
n = int(input("enter the number of fibonacci series:-"))
a =-1
b=1
fibonacci(n,a,b)

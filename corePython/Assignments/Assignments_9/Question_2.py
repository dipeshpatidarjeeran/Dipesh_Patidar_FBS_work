"""
    Write a program to check if given number is Armstrong or not using recursive
    function.
"""
def digit(n):
    if n==0:
        return 0
    else:
        return 1+digit(n//10)

def armstrong(n, p):
    if n==0:
        return 0
    else:
        a = n%10
        arm = a**p
        return arm+armstrong(n//10,p)

n = int(input("enter the number:-"))
p = digit(n)
print(armstrong(n,p))
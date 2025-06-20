"""
    Write a program to check whether a number is prime or not using recursion.
"""
def prime(n,i=2):

    if n%i ==0:
        return False
    if i*i>n:
        return True
    return prime(n,i+1)

n = int(input("enter the number:-"))
obj=prime(n)

if obj:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not prime number")
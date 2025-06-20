"""
    Write a program to reverse a number using recursion.
"""
def reverse(n,rev=0):
    if n==0:
        return rev
    else:
        return reverse(n//10,rev*10+n%10)
    
n = int(input("enter the number:-"))
print(reverse(n))
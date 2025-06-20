"""
    Write a program to reverse a given number using recursive function.
"""
def reverse(n,rev=0):
    if n==0:
        return rev
    else:
        # digit = n%10
        # rev = rev*10 +digit 
        return reverse(n//10,rev*10+n%10)
    
n = int(input("enter the number:-"))
print(reverse(n))
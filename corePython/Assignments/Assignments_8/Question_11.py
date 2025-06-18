"""
    WAP to check if a given number is Armstrong number or not. For
    each task create separate functions.
"""
def power(p):
    count=0
    while(p>0):
        count+=1
        p//=10
    return count

def armstrong(n):
    p = power(n)
    sum = 0
    while(n>0):
        digit = n%10
        sum+=digit**p
        n//=10
    return sum

n = int(input("enter the number:-"))
arm = armstrong(n)
if arm == n:
    print(f'{n} is a armstrong number.')
else:
    print(f'{n} is not armstrong number.')
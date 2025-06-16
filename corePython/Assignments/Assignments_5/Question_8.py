"""
    Write a program to solve the following series :
    a. 1! + 2! + 3! + 4! + .....n!
    b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
    c. Find the sum of a geometric series from 1 to n where 
        the common ratio is 2.
    d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
    e. x - x2/3 + x3/5 - x4/7 + .... to n terms
"""
# a.
n=int(input("enter the number of series:-"))
sum=0
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact*=j
    sum+=fact
print(f"1! + 2! + 3! + .....{n}! = {sum}")

# # b.
n=int(input("enter the number of series:-"))
sum=0
for i in range(1,n+1):
    sum+=n**i
print(f"{n} + {n}^2 + {n}^3 + .....+{n}^{n} = {sum}")

# c.
n=int(input("enter the number of geometric series:-"))
sum=0
for i in range(n):
    a = 2**i
    sum+=a
print(f"sum of geometric series = {sum}")

# d.
a=int(input("enter the number of value a:-"))
sum=0
for i in range(1,11):
    b = (a**i)/i
    sum+=b
print(f"{a} + {a}2 / 2 + {a}3 / 3 + ...... + {a}10 / 10 = {sum}")

# e.

x = int(input("enter the value of x:-"))
n = int(input("enter the number of terms:-"))
sum = 0
for i in range(1,n+1):
    if i%2 ==0:
        sum-=(x**i)/(2*i-1)
    else:
        sum+=(x**i)/(2*i-1)
print("x - x2/3 + x3/5 - x4/7 + .... = ",sum)
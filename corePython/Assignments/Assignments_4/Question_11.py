"""
    Write a program to check if given number Strong Number.
"""
#  sum of the factorials of its digits equals the number itself. 145

n = int(input("enter the number:-"))
sum = 0
number = n
while(n>0):
    fact =1
    a = n%10
    for i in range(1, a+1):
        fact *= i
    sum += fact
    print(fact)
    n = n//10

if number == sum:
    print(f"{number} is strong number")
else:
    print(f"{number} is not strong number")
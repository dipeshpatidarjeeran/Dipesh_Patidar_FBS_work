"""
    WAP to print sum of series upto n.
"""
n = int(input("enter the number:-"))
sum = 0
for i in range(1,n+1):
    sum += i

print(f"sum is {sum}")
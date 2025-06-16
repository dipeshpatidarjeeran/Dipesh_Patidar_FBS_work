"""
    Write a program to check if given number is Perfect Number.
"""
# Example 6 → Divisors: 1, 2, 3
# Sum = 1 + 2 + 3 = 6  → Perfect Number

n = int(input("enter the number:-"))
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum+=i
print(sum)
if n == sum:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not perfect number")
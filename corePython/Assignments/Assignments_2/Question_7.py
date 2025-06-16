"""
    Find the sum of three-digit number.
"""
num = int(input("enter the number:-"))
sum = 0

while(num>10):
    sum += num%10
    num = num//10
sum += num%10

print(f"sum of digits is {sum}")
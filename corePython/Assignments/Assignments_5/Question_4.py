"""
    Write a program to check if given number is Armstrong number or not.
    (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
    4*4*4*4)
"""
n = int(input("enter the armstrong number:-"))
power = len(str(n))
sum = 0
arm = n 

while(n>0):
    a = n%10
    sum+= a**power
    n = n//10

if arm == sum:
    print(f"given {arm} number is a armstrong number.")
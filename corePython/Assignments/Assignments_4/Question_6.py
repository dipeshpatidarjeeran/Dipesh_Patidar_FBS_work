"""
Write a program to check if a given number is prime number or not.
"""
n = int(input("enter the number:-"))
count = 0
for i in range(2,n):
    if n%i == 0:
        count+=1
    
if count ==0:
    print("the number is prime")
else:
    print("the number is not prime")
        
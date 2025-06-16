"""
    Write a program to reverse three-digit number.
"""
num = int(input("enter the number:-"))
str1 = ''
while(num>10):
    str1 += str(num%10)
    num = num//10
str1 += str(num%10)

print(f"reverse number is {str1}")

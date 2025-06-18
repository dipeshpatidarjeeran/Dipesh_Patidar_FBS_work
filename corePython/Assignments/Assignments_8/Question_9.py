"""
    Write a program to check if entered number is a palindrome or
    not.
"""
def palindrome(n):
    rev =0
    while(n>0):
        digit = n%10
        rev = rev*10 + digit
        n//=10

    return rev

num = int(input("enter the number:-"))
pal = palindrome(num)

if pal == num:
    print(f'{num} is a palindrome.')
else:
    print(f'{num} is not palindrome.')
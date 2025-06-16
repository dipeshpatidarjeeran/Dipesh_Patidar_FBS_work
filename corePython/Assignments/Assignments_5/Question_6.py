"""
    Write a program to print prime numbers between 1 to 100.
"""
for i in range(2,101):
    for j in range(2,(i+1)//2+1):
        if i%j == 0:
            break
    else:
        print(f"{i} is prime number")

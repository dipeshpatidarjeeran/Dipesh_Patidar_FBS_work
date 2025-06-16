"""
    Write a program to print first n prime numbers.
"""
n = int(input("enter how many prime numberas you want:-"))
count = 0
first_no = 2
while(n>count):
    for i in range(2,(first_no//2)+1):
        if first_no%i == 0:
            break
    else:
        print(first_no, end=' ')
        count+=1
    first_no+=1
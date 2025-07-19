num = int(input("how many prime number you want to print:-"))
count = 0
first_p = 2
while(num > count):
    for i in range(2,(first_p//2)+1):
        if first_p%i == 0:
            break
    else:
        print(first_p, end=' ')
        count += 1
    first_p += 1 
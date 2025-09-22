first = 2
num = int(input("enter the number for print prime number:-"))
count = 0
while(count < num):
    for i in range(2 ,first):
        if first%i == 0:
            first += 1
            break
    else:
        print("prime number:-",first)
        first += 1
        count += 1 
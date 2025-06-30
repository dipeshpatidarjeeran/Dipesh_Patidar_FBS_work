# Print 1 to 100 in snakes and ladder pattern.
num = 1
for i in range(1,11):
    li =[]
    for j in range(10):
        if i%2==0:
            li.append(num)
        else:
            print(num,end=' ')
        num+=1
    li.reverse()
    for j in li:
        print(j,end=' ')

    print()
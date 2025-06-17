k=1
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')

    for j in range(1,i+1):
        print(j,end=' ')
    k=i
    for j in range(1,i):
        print(k-1,end=' ')
        k-=1
    print()
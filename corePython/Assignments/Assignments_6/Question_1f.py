k=1
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,k+1):
        print(j,end=' ')
    k+=2
    print()
k=1
for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end=' ')

    for j in range(1,k+1):
        if j%2==0:
            print(' ',end=' ')
        else:
            print("*",end=' ')
    k+=2

    print()
k=7
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')

    for j in range(1,k+1):
        print(' ',end=' ')
    k-=2
    l=i
    for j in range(1,i+1):
        if i==5 and j==1:
            l-=1
        else:
            print(l,end=' ')
            l-=1
    print()
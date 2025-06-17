k=1
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')

    for j in range(1,k+1):
        if j==1 or j==k:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    k+=2
    print()
l=8
for i in range(1,5):
    for j in range(1,i+1):
        print(' ',end=' ')

   
    for j in range(1,l):
        if j==1 or l-1==j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    l-=2
    print()
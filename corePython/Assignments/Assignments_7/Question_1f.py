for i in range(1,6):
    for j in range(1,7-i):
        if j==1:
            print(i,end=' ')
        elif i == 1:
            print(j,end=' ')
        elif (i+j-1)==5:
            print(i+j-1,end=' ')
        else:
            print(' ',end=' ')

    print()
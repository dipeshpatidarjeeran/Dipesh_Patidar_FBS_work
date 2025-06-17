
for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end=' ')
    k=1
    for j in range(1,i+1):
        if j==1 or j==i:
            print(f'{k} ',end=' ')
        else:
            print('  ',end=' ')
        

    print()
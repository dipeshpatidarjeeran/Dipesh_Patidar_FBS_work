for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    
    for j in range(1,i+1):
        print((i+j-1),end=' ')
        
    k=(i-1)*2
    for j in range(1,i):
        print(k,end=' ')
        k-=1 
    
    print()
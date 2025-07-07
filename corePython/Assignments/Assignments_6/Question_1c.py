n=5
list1 =[[1]]
for i in range(n):
    p = list1[-1]
    pro = [0] + p + [0]
    new = []
    for j in range(len(pro)-1):
        new.append(pro[j]+pro[j+1])
    list1.append(new)

    for j in range(1,n-i):
        print(' ',end=' ')
    for j in range(i+1):
        print(f' {list1[i][j]}',end=' ')

    print()
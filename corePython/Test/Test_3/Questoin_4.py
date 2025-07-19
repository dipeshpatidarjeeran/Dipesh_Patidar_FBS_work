# 10101
# 01010
# 10101
# 01010
# 10101
a = 0
b = 1
for i in range(5):
    for j in range(5):
        if (i+j)%2 ==0:
            print(b,end=' ')
        else:
            print(a, end=' ')

    print()
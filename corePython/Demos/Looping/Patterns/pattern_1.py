# for i in range(1,6):
#     for j in range(1,6):
#         print("*", end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(i, end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(j, end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(chr(64+i), end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(chr(64+j), end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1, i+1):
#         print(i,end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,7-i):
#         print("*",end=' ')
#     print() 

# for i in range(1,6):
#     for j in range(1,7-i):
#         print(chr(64+i),end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i%2==0:
#             print("$",end=' ')
#         else:
#             print("*",end=' ')
#     print()


for i in range(1,6):
    for j in range(1,6):
        if i%2==0:
            if j%2!=0:
                print("$",end=' ')
            else:
                print("*",end=' ')
        else:
            if j%2==0:
                print("$",end=' ')
            else:
                print("*",end=' ')
    print()

for i in range(1,6):
    for j in range(1,6):
        if (i+j)%2==0:
            print("*",end=' ')
        else:
            print("$",end=' ')

    print()
n = int(input("enter the number:-"))
add = 0
for j in range(1,n+1):
    fact = 1
    for i in range(1,j+1):
        fact *= i
    a = j/fact
    add += a
print("1/!1 + 2/!2 + 3/!3 + ......N/!N:-",add)
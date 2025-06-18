"""
    Sum of all prime numbers between 1 to n
"""
def sum_prime(n):
    sum=0
    for i in range(2,n+1):
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            sum+=i
    return sum

n = int(input("enter the number:-"))
print("sum of prime numbers is :-",sum_prime(n))

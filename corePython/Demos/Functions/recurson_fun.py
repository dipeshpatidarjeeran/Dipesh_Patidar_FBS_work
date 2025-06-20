# write a program for sum of n number series
def sumOfSeries(n):
    if n==0:
        return 0
    else:
        return n+sumOfSeries(n-1)
    
n=int(input("enter number for sum of series:-"))
print("additoin:",sumOfSeries(n))


# write a program for factorial using recursive function
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
n=5
print(fact(n))
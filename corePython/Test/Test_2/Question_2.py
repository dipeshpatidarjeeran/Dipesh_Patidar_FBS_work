n = int(input("Enter the number:-"))

first = n//100
n = n % 100
second = n // 10
third = n % 10

if first == second*2 and first*2 == third:
    print("Yes,you have done it")
else:
    print("please try next time")
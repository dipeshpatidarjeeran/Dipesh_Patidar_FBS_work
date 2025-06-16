num1 = int(input("enter the first number:-"))
num2 = int(input("enter the second number:-"))
op = input("enter the operator(+,-,*,/):-")

if op=='+':
    print(f"addition is num1+num2 = {num1+num2}")
elif op=='-':
    print(f"subtration is num1-num2 = {num1-num2}")
elif op=='*':
    print(f"multiplication is num1*num2 = {num1*num2}")
elif op=='/':
    print(f"division is num1/num2 = {num1/num2}")
else:
    print("Invalid operator....")
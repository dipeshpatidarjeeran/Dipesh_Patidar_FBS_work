# write a program for arithmetic operations(+,-,*,/) using one function

def arithmetic_op():
    x = int(input("enter the first number:-"))
    y = int(input("enter the second number:-"))

    add = x+y
    sub = x-y 
    multi = x*y
    devi = x/y
    print("Addition:-",add)
    print("subtraction:-",sub)
    print("multiplication:-",multi)
    print("devision:-",devi)

arithmetic_op()
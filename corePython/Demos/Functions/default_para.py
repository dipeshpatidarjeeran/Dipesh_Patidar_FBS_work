## default parameter
#1. assign value to parameter in the function defination
#2. flow in right to left
#3. achieve optional parameter concept

def add(a,b,c=0):
    print(a+b+c)

add(1,2,3)

add(10, 20)     #positional parameter

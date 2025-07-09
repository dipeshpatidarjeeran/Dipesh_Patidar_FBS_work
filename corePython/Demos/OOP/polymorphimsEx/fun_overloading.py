# we cann't use function overloading in python because python is a interpreter language, code execute line by line
# function overloading working in compile type language 
# only overwrite function 

def sum(a,b):
    print("addition:",a+b)

def sum(a,b,c):
    print("addition:",a+b+c)

sum(10,20,20)
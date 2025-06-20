#### variable length / numbers of argument
#1. Mention asterisk(*) symbol before the parameter in function definition
#2. where we can pass multiple values to the function
#3. store data in tuple
#4. use for loop to iterate elements

def add(*data):
    sum=0
    for i in data:
        sum+=i
    return sum

res = add(10,20,30)
print("Additoin:-",res)

# wap for multiplication with multiple values

def multiplication(*data):
    multi = 1
    for i in data:
        multi *= i
    return multi

res = multiplication(5,8,3)
print("Multiplication:-",res)
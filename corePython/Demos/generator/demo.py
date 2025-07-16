### Generator
#1. generating values
#2. according to programer
#3. maintaining sate of function
#4. memory management
#5. we use yield keyword

def fun():
    for i in range(1,11):
        yield i    

res = fun()

print(next(res))

print("other lines of code")

print(next(res))
print(next(res))
print(next(res))
print(next(res))

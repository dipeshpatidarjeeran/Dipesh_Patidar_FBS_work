#### Map Function
#1. for multiple output you can use the map function
#2. map(function, iterabless)
#3. map function return objects and then convert list, tuple set, etc

data = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda x: x**2, data))
print(res)


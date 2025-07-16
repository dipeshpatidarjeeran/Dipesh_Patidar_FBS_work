#### filter
#1. filter(function, iterables)
#2. use for filter the values in the iterables
#3. filter function return objects and then convert list, tuple set, etc

data = [1,2,3,4,5,6,7,8,9,10]
res = list(filter(lambda num: num % 2 == 0, data))
print(res)


data = [1,-2,3,-4,5,6,-7,8,9,10]
res = list(filter(lambda num: num > 0, data))
print(res)
# Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.

dict1 = {}
def cacheDecorator(fun):
    def wrapper(a):
        if a in dict1:
            print(f"fetching from cache for {a}")
            return dict1[a] 
        fun(a)
    return wrapper


@cacheDecorator
def myFun(a):
    cube = a**3
    dict1[a] = cube
    print(f"{a} cube is:",dict1[a])

myFun(5)
myFun(6)
print(myFun(5))
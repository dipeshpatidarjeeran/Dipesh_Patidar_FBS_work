# Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.

def cacheDecorator(fun):
    def wrapper():
        print("this is wrapper function.")
        fun()
    return wrapper


@cacheDecorator
def myFun():
    print("this is my function")

myFun()
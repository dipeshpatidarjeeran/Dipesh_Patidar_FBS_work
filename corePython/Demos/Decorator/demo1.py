# user define decorator
def myDecorator(fun):
    def wrapper():
        print("this is wrapper function.")
        fun()
    return wrapper

@myDecorator
def greet():
    print("Good Morning!")

greet()
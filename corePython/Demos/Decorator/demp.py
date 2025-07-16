def demo():
    print("this is demo function.")

fun = demo

del demo
fun()


# manual decorator
def greet():
    print("Good Morning!")

def fun(a):
    print("this is fun function")
    a()

fun(greet)
 
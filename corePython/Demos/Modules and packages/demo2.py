n =26

# method1
# from mypackage import checkFunction
# print(checkFunction.checkEven(n))

# method2
# from mypackage.checkFunction import *
# print(checkEven(n))

# method3
# from mypackage.checkFunction import checkEven
# print(checkEven(n))

# method4
from mypackage.checkFunction import checkEven as CE
print(CE(n))
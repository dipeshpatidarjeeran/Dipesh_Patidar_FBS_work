#1. structure - denoted by (,)
# tu = (10,)
# print(type(tu))

#2. Heterogenous
tu = (101,'dipesh',400000.0)
print(type(tu))

#3. ordered
print(tu)

#4. Immutable
# tu[0] = 102  # given typeError: item assignment does not support
print(tu)

#5. Faster the list

import sys
li = []
tu = tuple()
print(sys.getsizeof(li))
print(sys.getsizeof(tu))
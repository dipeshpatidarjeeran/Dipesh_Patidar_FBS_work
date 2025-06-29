# write a program to ad element in tuple

tu = (10,20,30,40)
ele = 50

li = list(tu)
# print(li)
li.append(ele)
# print(li)

tu = tuple(li)
print(tu)
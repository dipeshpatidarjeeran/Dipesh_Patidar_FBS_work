# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged
str1 = 'diepsh'
new = ''
for i in range(len(str1)):
    if i == 0:
        new += str1[len(str1)-1]
    elif i == len(str1)-1:
        new += str1[0]
    else:
        new += str1[i]

print(f'"{str1}" exchange first and last charactor:{new}')
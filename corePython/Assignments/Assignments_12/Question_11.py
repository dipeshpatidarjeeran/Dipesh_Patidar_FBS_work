# Python Program to replace every blank space with hyphen in a string.
str1 = 'this is first line'
new = ''
for i in str1:
    if i == ' ':
        new += '-'
    else:
        new += i

print('add hyphen(-) in blank space:',new)
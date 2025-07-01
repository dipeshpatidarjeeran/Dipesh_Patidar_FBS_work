# Python Program to Take in a String and Replace Every Blank Space
# with Hyphen
str1 = 'this is first line'
new = ''
for i in str1:
    if i == ' ':
        new += '-'
    else:
        new += i

print('add hyphen(-) in blank space:',new)
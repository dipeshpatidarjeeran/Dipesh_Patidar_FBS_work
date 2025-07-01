# Python Program to Remove the Characters of Odd Index Values in a
# String
str1 = 'program'
new = ''
for i in range(len(str1)):
    if i%2 == 0:
        new += str1[i]

print(f'"{str1}" remove odd indexing values and new string: {new}')
# Python Program to count number of lowercase characters in a string.
str1 = 'This Is Tree'
count = 0
for i in str1:
    if i.islower():
        count += 1

print(count)
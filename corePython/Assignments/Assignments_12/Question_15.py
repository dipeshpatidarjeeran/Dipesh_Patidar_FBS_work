# Python Program to find larger string without using built-in functions.
str1 = 'python'
str2 = 'java'
count1 = 0
count2 = 0
for i in str1:
    count1 += 1
for i in str2:
    count2 += 1

if count1 > count2:
    print(f'large string is "{str1}"')
elif count1 < count2:
    print(f'large string is "{str2}"')
else:
    print("both string are equal")
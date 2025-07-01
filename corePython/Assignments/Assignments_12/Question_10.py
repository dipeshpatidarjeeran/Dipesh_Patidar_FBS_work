# Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions
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
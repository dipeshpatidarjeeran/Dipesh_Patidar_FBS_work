# Python Program to Count the Number of Vowels in a String
str1 = 'A program'
count = 0
for i in str1:
    if i.lower() in ['a','e','i','o','u']:
        count += 1

print(f"In '{str1}' string vowels count is {count}")
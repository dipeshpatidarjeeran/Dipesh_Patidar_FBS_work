# Python Program to Detect if Two Strings are Anagrams
str1 = 'listen'
str2 = 'silent'

for i in str1:
    if i not in str2 or (len(str1) != len(str2)) or str1.count(i) != str2.count(i):
        print(f'{str1} and {str2} are not anagrams')
        break
else:
    print(f"{str1} and {str2} are anagrams")
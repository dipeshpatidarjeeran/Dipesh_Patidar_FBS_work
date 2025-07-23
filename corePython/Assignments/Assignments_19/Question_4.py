# Remove all of the vowels in a string (take input from user)
str1 = input("Enter the string:-")
str2 = ''.join([i for i in str1 if i not in "aeiou"])
print(str2)
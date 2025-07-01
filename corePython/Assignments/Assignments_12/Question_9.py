# Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String
str1 = "this is first line"
str2 = str1.split(" ")
str3 = str1.replace(' ', '')

print(str1)
print(f"In this string total words are {len(str2)} and charactors are {len(str3)}")

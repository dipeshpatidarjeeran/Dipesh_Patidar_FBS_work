# Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary
str1 = "the apple banana the apple orange banana the apple"
word = str1.split()
f = {}
for i in word:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1

print(f"count the frequency of words in string using a dict {f}")
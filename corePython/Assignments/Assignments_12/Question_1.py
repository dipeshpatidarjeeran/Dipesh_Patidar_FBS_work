# Python Program to Replace all Occurrences of ‘a’ with $ in a String
str1 = 'program to Replace'
new = ''
for i in str1:
    if i == 'a':
        new += "$"
    else:
        new += i
    
print("Replace all occurrences of 'a' with $ in new string:",new)
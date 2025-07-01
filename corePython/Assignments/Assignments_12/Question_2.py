# Python Program to Remove the nth Index Character from a Non-Empty string
str1 = 'program'
re_ind = 3
new = ''
for i in range(len(str1)):
    if i != re_ind:
        new += str1[i]

print(f"Remove the {re_ind} index in {str1} string and then new string:",new)
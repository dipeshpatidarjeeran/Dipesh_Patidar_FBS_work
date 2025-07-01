# Python Program to count number of digits and letters in a string.
str1 = "asdf@ 123"
num_count = 0
alpha_count = 0
for i in str1:
    if i.isdigit():
        num_count += 1
    elif i.isalpha():
        alpha_count += 1

print(str1)
print(f'In this string digit count is {num_count} and letters count {alpha_count}')
# Count the number of spaces in a string (take input from user)
str1 = input("Enter the any sentance:-")
# count = 0
# for i in str1:
#     if i == ' ':
#         count += 1
# print(count)
count = len([i for i in str1 if i == ' '])
print(count)
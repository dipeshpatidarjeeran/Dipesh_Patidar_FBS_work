# Find all of the words in a string that are less than 5 letters (take
# input from user)
str1 = input("enter the any sentance:-")
# li = str1.split()
# for i in li:
#     if len(i) < 5:
#         print(i)

li = [i for i in str1.split() if len(i) < 5]
print(li)
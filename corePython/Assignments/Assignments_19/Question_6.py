# Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)
str1 = input("enter the any sentance:-")
di = {i:len(i) for i in str1.split()}
print(di)
# Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.
list1 = ['the cat dog the', 'dog the cat dog the','cat the dog']

li = []
t = []
for str1 in list1:
    str2 = str1.split(' ')
    for i in range(len(str2)):
        if str2[i] in li:
            ind = li.index(str2[i])
            t[ind] += 1
        else:
            li.append(str2[i])
            t.append(1)
        
print("count word in a string",li,t)

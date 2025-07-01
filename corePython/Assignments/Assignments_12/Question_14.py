# Python Program to count the occurrences of ach word in a string.
str1 = 'the cat dog the dog the cat dog the'
str2 = str1.split(' ')
li = []
t = []
for i in range(len(str2)):
    if str2[i] in li:
        ind = li.index(str2[i])
        t[ind] += 1
    else:
        li.append(str2[i])
        t.append(1)
        
print("count word in a string",li,t)
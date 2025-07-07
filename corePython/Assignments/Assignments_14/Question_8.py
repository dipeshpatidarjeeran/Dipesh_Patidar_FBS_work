# Write a Python program to find all the anagrams and group them
# together from a given list of strings.
str1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
dict1 ={}
for i in range(len(str1)):
    g = [str1[i]]
    for j in range(len(str1)):
        if j !=i:
            for k in str1[i]:
                if k not in str1[j] or (len(str1[i]) != len(str1[j])) or str1[i].count(k) != str1[j].count(k):
                    break
            else:
                g.append(str1[j])

    dict1[str1[i]] = g
print(dict1)

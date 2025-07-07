# Write a Python program to find the longest common prefix of all
# strings. Use the Python set.
s1 = {"flower", "flow", "flight"}
str1 = ''
li = list(s1)
min_len = len(li[0])
ind = 0
for i in range(len(li)):
    if len(li[i]) < min_len:
        min_len = len(li[i])
        ind = i

for i in range(len(li[ind])):
    let = li[ind][i]
    for word in li:
        if let != word[i]:
            break
    else:
        str1 += let
        

print(str1)
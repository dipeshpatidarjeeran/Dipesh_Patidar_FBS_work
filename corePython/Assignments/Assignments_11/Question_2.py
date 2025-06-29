"""
    Python Program to Merge Two Lists and Sort it
"""
li1 = [5,2,4,3]
li2 = [7,1,6,8]

for i in li2:
    li1.append(i)

for i in range(len(li1)-1):
    ind = i
    for j in range(i+1,len(li1)):
        if li1[j] < li1[ind]:
            ind = j

    li1[i],li1[ind] = li1[ind],li1[i]

print("sorted list:",li1)

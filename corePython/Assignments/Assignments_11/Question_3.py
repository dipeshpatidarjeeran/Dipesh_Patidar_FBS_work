# Python Program to Sort the List According to the Second Element in Sublist
li = [[5,2],[6,1],[5,4],[6,3]]
for i in range(len(li)-1):
    ind = i
    for j in range(i+1,len(li)):
        if li[j][1] < li[ind][1]:
            ind = j
    li[i],li[ind] = li[ind],li[i]

print("Sorted list According to the second element in sublist:",li)
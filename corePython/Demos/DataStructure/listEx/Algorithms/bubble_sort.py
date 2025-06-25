def bubbleSort(li):
    for i in range(1,len(li)):
        for j in range(len(li)-i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li

li = [50,60,20,30,40,10]
print(bubbleSort(li)) 
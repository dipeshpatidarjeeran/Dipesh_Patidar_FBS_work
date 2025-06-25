def selectionSort(li):
    for i in range(len(li)-1):
        ind = i
        for j in range(i+1,len(li)):
            if li[j] < li[ind]:
                ind =j
        li[i], li[ind] = li[ind], li[i]
    return li

li = [60,40,10,70,30,20,50]
print("selection sort:",selectionSort(li))
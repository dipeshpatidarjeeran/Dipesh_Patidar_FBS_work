def binarySearch(li, search_ele):
    beg = 0
    end = len(li)-1
    while(beg<=end):
        print("loop executed")
        mid = (beg+end)//2
        if(search_ele == li[mid]):
            return mid
        elif(search_ele < li[mid]):
            end = mid - 1
        elif(search_ele > li[mid]):
            beg = mid + 1
    else:
        return -1
    
li =[10,30,40,50,60,70]
ele = int(input("enter the element for search:-"))
res = binarySearch(li,ele)
if res != -1:
    print(f"{ele} is found at the index {res}.")
else:
    print(f"{ele} is not found in the list.")

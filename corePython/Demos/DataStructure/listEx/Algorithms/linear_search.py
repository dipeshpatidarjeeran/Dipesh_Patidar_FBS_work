def linearSearch(li,search_ele):
    for i in range(len(li)):
        if (search_ele == li[i]):
            return i
    else:
        return -1
    
li = [23,43,22,4,6,5]
ele = int(input("enter the number for search:-"))
res = linearSearch(li,ele)
if res != -1:
    print(f"{ele} is found at the index {res}.")
else:
    print(f"{ele} is not found in the list.")
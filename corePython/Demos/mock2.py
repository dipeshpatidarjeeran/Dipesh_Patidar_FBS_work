# li = [3,5,2,3,5]
# new_list = []
# for i in range(len(li)):
#     if li[i] not in new_list:
#         new_list.append(li[i])
# print(new_list)


# li = [20,30,10,40,50]

# for i in range(len(li)-1):
#     ind = i
#     for j in range(i,len(li)):
#         if li[i] > li[j]:
#             ind = j
#     li[i],li[ind] = li[ind],li[i]

# print(li)


def even():
    n = 1
    while True:
        if n %2 ==0:
            yield n
        n += 1

e = even()
print(next(e))
print(next(e))
print(next(e))

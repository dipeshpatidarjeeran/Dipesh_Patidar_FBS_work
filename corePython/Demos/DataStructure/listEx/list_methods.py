li = [30,40,10,20]

#li.append(50)
# li.clear()
# li2 = li.copy()
# li3 = li
# li.append(50)
# print(li.index(50))
# print(li2)

# print(li.count(31))
# print(li.count(10))

# print(li.extend([1,2,3,4]))

# li.insert(0,50)
# print(li)

# li.pop(0)
# print(li)

# li.remove(10)
# print(li)

# li.reverse()
# print(li)

# li.sort()
# print(li)
# li.sort(reverse=True)
# print(li)

li = [70,80,[10,20,30],[40,50,60]]

# for i in range(len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j], end=' ')
#     print()

sum = 0 
for sub_list in li:
    print(sub_list)
    if type(sub_list) == int:
        sum += sub_list
    else:
        for ele in sub_list:
            sum += ele

print("addtion:",sum)
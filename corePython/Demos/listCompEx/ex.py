# list1 =[]
# for i in range(1, 11):
#     list1.append(i)

# list1 = [i for i in range(1,11)]
# print(list1)


list1 =[]
for i in range(1, 11):
    if i%2 ==0:
        list1.append(i)

print(list1)

list2 = [i for i in range(1,11) if(i%2==0)]
print(list2)
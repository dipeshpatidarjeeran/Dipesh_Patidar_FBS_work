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

list2 = [[i for i in range(i-9,i+1)] for i in range(10,101,10)]
print(list2)

list2 = [[i for i in range((i*10)-9,i*10+1)] for i in range(1,11)]
print(list2)

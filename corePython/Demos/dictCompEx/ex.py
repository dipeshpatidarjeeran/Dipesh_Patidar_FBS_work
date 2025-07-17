# dict1 ={}

# for i in range(1,11):
#     # dict1[i] = i**2
#     dict1.update({i:i**2})

# print(dict1)

dict1 = {i:i**2 for i in range(1,11)}
print(dict1)


dict2 = {i:i**2 for i in range(1,11) if(i%2==0)}
print(dict2)

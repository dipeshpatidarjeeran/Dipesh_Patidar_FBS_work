# A list contains sublist with Emp information as follows :
# Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
# [210,”Tannu”,14000],[320,”Suresh”,35000]]
# Write a program to sort the list based on salary.

Data = [[101,"Seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,"Suresh",35000]]

for i in range(len(Data)-1):
    ind = i
    for j in range(i,len(Data)):
        if Data[ind][2] > Data[j][2]:
            ind = j
    Data[i],Data[ind] = Data[ind],Data[i]

print(Data)
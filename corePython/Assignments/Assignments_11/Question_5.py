# Python Program to Sort a List According to the Length of the Elements within the list.
li = ['hello','worlds','dipesh','hi']

for i in range(len(li)-1):
    ind = i
    for j in range(i+1,len(li)):
        if len(li[j]) < len(li[ind]):
            ind = j
    li[i],li[ind] = li[ind],li[i]

print(f"sort a listaccording to length of element:{li}")

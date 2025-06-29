# Python Program to Find the Second Largest Number in a List Using Bubble sort
li = [4,3,2,6,7]
for i in range(1,len(li)):
    for j in range(len(li)-i):
        if li[j] < li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]

print(f"Second largest number in list{li} is:",li[1])
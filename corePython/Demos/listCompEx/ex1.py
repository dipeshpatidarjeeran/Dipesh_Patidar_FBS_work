list1 = [i**3 for i in range(1,11) if(i%2==0)]
print(list1)


# print positive number in range(-10, 10)
li = [-1,3,-4,2,-6,5]
list1 = [i for i in range(-10, 10) if(i>0)]
print(list1)


# print even number in the tuple
t = (1,10,2,9,20,25,38)
list1 = [i for i in t if(i%2==0)]
print(list1) 
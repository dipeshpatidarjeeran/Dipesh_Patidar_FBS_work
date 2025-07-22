import random

#### get random number between 0 to 1
# print(random.random())


#### get integer number between a to b
# print(random.randint(1,100))


#### get float number between a to b
# print(random.uniform(5,15))


#### choice from the list
# li = [1,2,4,'a',4.3]
# print(random.choice(li))


#### get n random number with replacement and also get dublicate value
# li = [1,2,4,'a',4.3]
# print(random.choices(li, k=3))


#### get n unique number and not get dublicate value
# li = [1,2,4,'a',4.3]
# print(random.sample(li, k=3))


#### change the position of item in the list
li = [1,2,4,'a',4.3]
random.shuffle(li)
print(li)
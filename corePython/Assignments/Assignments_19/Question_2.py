# Find all of the numbers from 1–1000 that have a 6 in them
# for i in range(1, 1001):
#     st = str(i)
#     if '6' in st:
#         print(i,end=', ')

li = [i for i in range(1, 1001) if '6' in str(i)]
print(li)
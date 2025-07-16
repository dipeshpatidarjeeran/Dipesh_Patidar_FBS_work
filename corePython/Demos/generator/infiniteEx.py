def infinite():
    i = 0 
    while True:
        i += 1
        yield i

res = infinite()

for i in res:
    print(i)
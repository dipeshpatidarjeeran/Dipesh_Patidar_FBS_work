# data = [4,6,5,3,2]

# mapdata = map(lambda x : x**3, data)
# li = list(mapdata)
# print(li)

# even = filter(lambda x : x % 2 == 0,data)
# li = list(even)
# print(li)

# from functools import reduce

# val = reduce(lambda x, y : x * y , data)
# print(val)


# from abc import ABC, abstractmethod

# class vahicle(ABC):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(vahicle):
#     def __init__(self, name, color, price):
#         super().__init__(name, color)
#         self.price = price

#     def stop(self):
#         print("car is stop")

# c = Car("BMW", "black", 4500000)
# c.stop()

def fab():
    a = -1
    b = 1
    while True:
        c = a + b
        yield c
        a = b
        b = c

f = fab()
print(next(f))


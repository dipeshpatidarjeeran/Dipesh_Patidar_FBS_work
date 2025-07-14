class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __add__(self, other):
        s = self.s + other.s
        m = s // 60
        s = s % 60

        m = m + self.m + other.m
        h = m // 60
        m = m % 60

        h = h + self.h + other.h
        return f'{h} : {m} : {s}'

t1 = Time(20,25,30)
t2 = Time(15,45,35)

print(t1 + t2)
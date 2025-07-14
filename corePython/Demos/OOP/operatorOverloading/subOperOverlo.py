class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __sub__(self, other):
        s1 = self.h*3600 + self.m*60 + self.s
        s2 = other.h*3600 + other.m*60 + other.s
        s = abs(s1 - s2)
        h = s // 3600
        s = s % 3600
        m = s // 60
        s = s % 60


        return f'{h} : {m} : {s}'

t1 = Time(20,25,30)
t2 = Time(15,45,35)

print(t2 - t1)
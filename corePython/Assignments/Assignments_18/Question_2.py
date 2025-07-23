# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
    # a. Constructor
    # b. Destructor
    # c. Overload +,- operator
class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __del__(self):
        print("Destructor is called.")

    def __add__(self, other):
        cm = self.km * 100000 + self.m * 100 + self.cm
        cm1 = other.km * 100000 + other.m * 100 + other.cm
        to_cm = cm + cm1
        km = to_cm // 100000
        cm = to_cm % 100000
        m = cm // 100
        cm = cm % 100

        return f"{km}Km {m}m {cm}cm"

    def __sub__(self, other):
        cm = self.km * 100000 + self.m * 100 + self.cm
        cm1 = other.km * 100000 + other.m * 100 + other.cm
        if cm > cm1:
            to_cm = cm - cm1
        else:
            to_cm = cm1 - cm
        km = to_cm // 100000
        cm = to_cm % 100000
        m = cm // 100
        cm = cm % 100

        return f"{km}Km {m}m {cm}cm"



d1 = Distance(1,500,50)
d2 = Distance(0,700,80)

d3 = d1 + d2
print(d3)

d4 = d1 - d2
print(d4)
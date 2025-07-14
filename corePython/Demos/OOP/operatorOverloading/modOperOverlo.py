class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mod__(self, other):
        a1 = self.a % other.a
        a2 = self.b % other.b
        return f"{a1, a2}"

e1 = Example(20,25)
e2 = Example(5,7)

print(e1 % e2)


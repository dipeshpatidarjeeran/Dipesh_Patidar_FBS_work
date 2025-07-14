class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        a1 = self.a * other
        a2 = self.b * other
        return f"{a1, a2}"

e1 = Example(20,25)
e2 = e1 * 3
print(e2)


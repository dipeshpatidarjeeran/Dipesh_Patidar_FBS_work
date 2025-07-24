# 1. Create a class Complex Number with data members as real and imag and add
# following methods :
    # a. Constructor
    # b. Destructor
    # c. Overload +,- operator

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("Destructor is called.")

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return f'{real} + {imag}'

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return f'{real} + {imag}'

    def display(self):
        return f"{self.real} + {self.imag}"

c1 = Complex(10,20j)
c2 = Complex(3,15j)

c3 = c1 + c2
print(c3)

c4 = c1 - c2
print(c4)
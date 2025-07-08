#### hierarchical inheritance 
from shape import Shape
class Rectangle(Shape):
    def __init__(self, Id, area, length, breadth):
        super().__init__(Id, area)
        self.l = length
        self.b = breadth

    def display(self):
        super().display()
        print("Length:",self.l)
        print("Breadth:",self.b)

r1 = Rectangle('r2',154,22,7)
r1.display()
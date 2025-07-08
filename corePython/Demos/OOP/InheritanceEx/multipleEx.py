#### Multiple Inheritance
#1. In multiple inheritance, the method of the first parent class (from left to right) is called 
#   if both parent classes define the same method name.
class A:
    def display(self):
        print("Display method of class A")

class B:
    def display(self):
        print("Display method of class B")

class C(A, B):
    def show(self):
        print("show method of class C")

c1 = C()
c1.display()
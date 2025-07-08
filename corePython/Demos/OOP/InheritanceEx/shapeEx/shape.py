#### hierarchical inheritance 
class Shape:
    def __init__(self, Id, area):
        self.id = Id
        self.area = area

    def display(self):
        print("Id:",self.id)
        print("Area:",self.area)

# s1 = Shape("s1",400)
# s1.display()

        
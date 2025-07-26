class Emp:
    def __init__(self, Id, name, dept, sal):
        self.Id = Id
        self.name = name
        self.dept = dept
        self.sal = sal

    def __str__(self):
        return f'Id:{self.Id}, Name:{self.name}, Dept:{self.dept}, Sal:{self.sal}'
    
if __name__ == "__main__":
    e1 = Emp(101,"abc",'DS', 34000)
    print(e1)
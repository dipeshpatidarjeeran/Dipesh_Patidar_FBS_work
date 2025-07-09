# str method always return data in string format.
# if use str method we should use return 
class Emp:
    def __init__(self, id , name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def __str__(self):
        return f'Id:{self.id}\nName:{self.name}\nSalary:{self.sal}'
    
e1 = Emp(101,'dipesh',150000)
print(e1)
print(e1.__dict__)   # return all attributes/state in the form of dictionary

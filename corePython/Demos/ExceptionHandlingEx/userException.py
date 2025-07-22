class UserException(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'{self.age} is not valid age'
    
class NameException(Exception):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'{self.name} is not valid name'
    
if __name__ == "__main__":
    ue = UserException(0)
    print(ue)
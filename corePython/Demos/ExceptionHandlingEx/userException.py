class UserException(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'{self.age} is not valid age'
    
if __name__ == "__main__":
    ue = UserException(0)
    print(ue)
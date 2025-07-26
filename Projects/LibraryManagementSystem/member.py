class Member:
    def __init__(self, Id, name, branch, phone, fine):
        self.mid = Id
        self.name = name
        self.branch = branch
        self.phone = phone
        self.fine = fine
        
    def __str__(self):
        return f'{self.mid}, {self.name}, {self.branch}, {self.phone}, {self.fine}'
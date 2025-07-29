class Member:
    def __init__(self, Id, name, branch, age, address, phone, fine, mstatus):
        self.mid = Id
        self.name = name
        self.branch = branch
        self.age = age
        self.address = address
        self.phone = phone
        self.fine = fine
        self.mstatus = mstatus
        
    def __str__(self):
        return f'{self.mid}, {self.name}, {self.branch}, {self.age}, {self.address}, {self.phone}, {self.fine}, {self.mstatus}'
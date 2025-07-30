import random

class Transaction:
    def __init__(self, amount, user_id, date, ptype):
        self.tid = random.randint(1000,9999)
        self.amount = amount
        self.user_id = user_id
        self.date = date
        self.ptype = ptype
        
    def __str__(self):
        return f'{self.tid}, {self.amount}, {self.user_id}, {self.date}, {self.ptype}'
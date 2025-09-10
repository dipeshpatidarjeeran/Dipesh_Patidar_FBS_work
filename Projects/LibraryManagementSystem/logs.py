import random, datetime

class Logs:
    def __init__(self, action, details):
        self.tid = random.randint(1000,9999)
        self.action = action
        self.details = details
        self.date = str(datetime.date.today())
        
        
    def __str__(self):
        return f'{self.tid}, {self.action}, {self.details}, {self.date}'
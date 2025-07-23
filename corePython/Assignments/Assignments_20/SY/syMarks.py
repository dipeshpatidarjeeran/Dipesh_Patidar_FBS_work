class SyMarks:
    def __init__(self, computer, maths, electronics):
        self.computer = computer
        self.maths = maths
        self.electronics = electronics

    def total_syMarks(self):
        total_SY = self.computer + self.maths + self.electronics
        return total_SY
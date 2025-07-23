class TyMarks:
    def __init__(self, theory, practical):
        self.theory = theory
        self.practical = practical

    def total_tyMarks(self):
        total_TY = self.theory + self.practical
        return total_TY
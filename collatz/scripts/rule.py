class Rule:
    def __init__(self, number):
        self.number = number

    def even(self):
        return int(self.number/2)

    def odd(self):
        return self.number*3 + 1
    
    def collatz_sequence(self):
        sequence = [self.number]
        while self.number != 1:
            if self.number % 2 == 0:
                self.number = self.even()
            else:
                self.number = self.odd()
            sequence.append(self.number)
        return sequence
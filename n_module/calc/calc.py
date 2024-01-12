class Calculator:
    def __init__(self, number1: int, number2: int):
        self.number1 = number1
        self.number2 = number2

    def add(self) -> int:
        return self.number1 + self.number2

    def sub(self) -> int:
        return self.number1 - self.number2



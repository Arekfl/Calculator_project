class Calculator:
    def __init__(self, op1: float, op2: float) -> None:
       self.op1 = op1
       self.op2 = op2
    def sum(self) -> float:
        return self.op1 + self.op2
    def subtract(self) -> float:
        return self.op1 - self.op2
    def multiply(self) -> float:
        return self.op1 * self.op2
    def divide(self) -> float:
        if self.op2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return self.op1 / self.op2
    
#calculator = Calculator(1, 0)
#print(calculator.sum())
#print(calculator.subtract())
#print(calculator.multiply())
#print(calculator.divide())

def _demo() -> None:  # pragma: no cover
    calc = Calculator(10, 0)
    print("sum:", calc.sum())
    print("subtract:", calc.subtract())
    print("multiply:", calc.multiply())
    try:
        print("divide:", calc.divide())
    except ZeroDivisionError as e:
        print("divide raised:", e)

if __name__ == "__main__":  # pragma: no cover
    _demo()


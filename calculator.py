import numpy


class calculator:

    def __init__(self,n1 ,oper ,n2):
        self.n1 = int(n1)
        self.operation = oper
        self.n2 = int(n2)



    def adding(self):

        result = self.n1 + self.n2
        return result
    

    def subbing(self):
        result = self.n1 - self.n2
        return result

    def multi(self):
        result = self.n1 * self.n2
        return result
    

    def dividing(self):
        if self.n2 == 0:
            print("cannot divide by zero")
            return
        result = self.n1 / self.n2
        return result

    def calculation(self):

        if self.operation == '+':
            result = self.adding()
        elif self.operation == "-":
            result = self.subbing()
        elif self.operation == "*":
            result = self.multi()
        elif self.operation == "/":
            result = self.dividing()

        print(result)


num1 = input("Enter first number: ")
operator = input("Choose an operation (+, -, *, /): ")
num2 = input("Enter second number: ")

test = calculator(num1, operator, num2)
test.calculation()

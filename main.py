class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1+self.num2
    def prod(self):
        return self.num1*self.num2
    
n1=int(input("enter number 1 "))
mycalc=calculator(n1,5)

print(mycalc.add())
print(mycalc.prod())
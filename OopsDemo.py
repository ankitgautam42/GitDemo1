class Calculator:
    num = 100    #class variable
    def __init__(self,a,b):         #constructor
        self.firstNumber=a          #instance variable
        self.SecondNumber=b
        print("I am called automatically when object is created")

    def getdata(self):
        print("i am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.SecondNumber + Calculator.num

obj = Calculator(2, 3)                # Object creation for class
obj.getdata()
print(obj.summation())

obj1 = Calculator(4, 5)                # Object creation for class
obj1.getdata()
print(obj1.summation())


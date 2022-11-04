import math


class Basic_Operator():
    def __init__(self,num1=0,num=0):
        self.num1 = input("Please input no 1: ")
        self.num2 = input("Please input no 2: ")

    def Add_Num(self):
        added = float(self.num1) + float(self.num2)
        return added
    def Subtract_Num(self):
        subtracted = float(self.num1) - float(self.num2)
        return subtracted
    def multiply(self):
        multiplied = float(self.num1)*float(num2)
    def division(self):
        divided = float(self.num1)/float(self.num2)


class Trigonometric():
    def __init__(self,num=0):
        self.num = float(input("Please Input a number: "))
    def Sine(self):
        d_sine = math.sin(self.num)
        return d_sine
    def Cosine(self):
        d_cosine = math.cos(self.num)
        return d_cosine
    def Hyp_Sine(self):
        d_sinh = math.sinh(self.num)
    def Hyp_Cosine(self):
        d_cosh = math.cosh(self.num)
    def Tangent(self):
        Tan = math.tan(self.num)
        return Tan
    def Hyp_Tan(self):
        tanh = math.tanh(self.num)
        return tanh


class Others():
    def __init__(self,num=0):
        self.num = float(input("Please inout a number: "))
    def Factorial(self):
        fact = math.factorial(self.num)
        return fact
    def Exponential(self):
        exp = math.exp(self.num)
        return exp
    def Log10(self):
        log = math.log10(self.num)
        return log
    def Sq_rt(self):
        d_sq = math.sqrt(self.name)
        return d_sq
    def Cube_rt(self):
        d_cube = (self.num)**(1/3)
        return d_cube

        




# Imports
import math


def calculate(x : int, y : int, method : str):
    if method == "add":
        return x+y
    elif method == "subtract":
        return x-y
    elif method == "multiply":
        return x*y
    elif method == "divide":
        return x/y
    elif method == "raise":
        return x**y
    else:
        return "Sorry the method you provided is invalid! Please try again."

class twoDimensionalVector():
    def __init__(self, x : int, y : int):
        self.direction = {'x': x, 'y': y}
        self.magnitude = math.sqrt(((x*x) + (y*y)))
    def __cv(self, x, y):
        d = {'x': x, 'y': y}
        m = math.sqrt(((x*x) + (y*y)))
        return {"direction": d, "magnitude": m}
    def __mul__(self, a):
        if (type(a) is int): # Caculates for scalar
            x = self.direction['x'] * a
            y = self.direction['y'] * a
            return self.__cv(x,y)
        elif (type(a) is twoDimensionalVector):
            print("Attempting to multiply a vector by a vector! Use the .dotProduct function to multiply vectors.")
            return
    def info(self):
        print("Your vector is:\n" + "Direction: <" + str(self.direction['x']) + ", " + str(self.direction['y']) + ">" + "\nMagnitude: " + str(self.magnitude))  
    def dotProduct(self, v):
        x = self.direction['x']*v.direction['x']
        y = self.direction['y']*v.direction['y']
        return x+y
        
        
a = 4
b = 8
vOne = twoDimensionalVector(calculate(a, b, 'add'), calculate(a, b, 'divide'))
vTwo = twoDimensionalVector(calculate(a, b, "multiply"), calculate(a, b, "subtract"))
print("\n\n\n")
vOne.info()
print("\n")
vTwo.info()
print("\n\n\n")
print(vOne.dotProduct(vTwo))
print("\n")
print(vTwo * 5)
print("\n")
vOne * vTwo
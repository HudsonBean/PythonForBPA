# Imports
import math

a = 1
b = 2
c = "Hello World!"
d = [a, b, c]

def caculate(x : int, y : int, method : str):
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



class Vector():
    def __init__(self, x : int, y : int):
        self.direction = {'x': x, 'y': y}
        self.magnitude = math.sqrt(((x*x) + (y*y)))
    def __call__(self):
        print("Your vector is:\n" + "Direction: <" + str(self.direction['x']) + ", " + str(self.direction['y']) + ">" + "\nMagnitude: " + str(self.magnitude))
        
v = Vector(3, 4)
v()

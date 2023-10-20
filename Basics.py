# Imports
import math


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
    def __cv(self, x, y):
        d = {'x': x, 'y': y}
        m = math.sqrt(((x*x) + (y*y)))
        return {"direction": d, "magnitude": m}
    def __mul__(self, a):
        if (type(a) is int): # Caculates for scalar
            x = self.direction['x'] * a
            y = self.direction['y'] * a
            return self.__cv(x,y)
        elif (type(a) is Vector):
            print("Attempting to multiply a vector by a vector! Use the .dotProduct or crossProduct function to multiply vectors.")
            return self
    def info(self):
        print("Your vector is:\n" + "Direction: <" + str(self.direction['x']) + ", " + str(self.direction['y']) + ">" + "\nMagnitude: " + str(self.magnitude))
        aOne = self.direction['x']
        aTwo = self.direction['y']
        
        bOne = v.direction['x']
        bTwo = v.direction['y']
        
        i = (aOne*bTwo)
        j = ((bOne*aTwo)*-1)
        
        return self.__cv(i,j)
    def dotProduct(self, v):
        x = self.direction['x']*v.direction['x']
        y = self.direction['y']*v.direction['y']
        return x+y
        
        
v = Vector(3, 4)
vTwo = Vector(8,1)
print(v.dotProduct(vTwo))

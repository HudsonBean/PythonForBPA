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
    def info(self):
        print("Your vector is:\n" + "Direction: <" + str(self.direction['x']) + ", " + str(self.direction['y']) + ">" + "\nMagnitude: " + str(self.magnitude))
    def __mul__(self, a):
        if (type(a) is int): # Caculates for scalar
            x = self.direction['x'] * a
            y = self.direction['y'] * a
            d = {'x': x, 'y': y}
            m = math.sqrt(((x*x) + (y*y)))
            return {"direction": d, "magnitude": m}
        
        elif (type(a) is Vector):
            debounce = False
            while (debounce == False):
                input1 = input("What method would you like?\n   (1) Cross-Product\n   (2) Dot-Product")
                if (input1 == 1):
                    debounce = True
                    print('Cross')
                elif (input1 == 2):
                    debounce = True
                    print('Dot')
                else:
                    debounce = False
                    print("The method you inputted was incorrect")
        
v = Vector(3, 4)
v * v
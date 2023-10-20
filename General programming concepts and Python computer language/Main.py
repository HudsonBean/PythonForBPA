a = 1
b = 2
c = "Hello World!"
d = [a, b, c]

print("We have 4 variables!")
print("The value of variable a is: " + str(a))
print("The value of variable b is: " + str(b))
print("The value of variable c is: " + c)
print("The value of variable c is: " + str(d))

def caculate(x, y, method):
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
print(str(caculate(a,b,"ada")))
#Imports
import random

# Version 1.0
def getRandomCombination():
    # Get dial ammount and combinations ammount
    DIAL_AMMOUNT = int(input("Each lock has how many dials?\n> "))
    COMBINATIONS_AMMOUNT = int(input("How many combinations should I generate?\n> "))
    Ans = []
    i = 0
    while i < COMBINATIONS_AMMOUNT:
        a = [] # Create blank table
        j = 0 # Reset number for loop
        while j < DIAL_AMMOUNT:
            list.append(a, random.randrange(0,10))
            j+=1
        list.append(Ans, a)
        i+=1 # Increase for next set of combinations
    return Ans
print(getRandomCombination())

# Version 2.0
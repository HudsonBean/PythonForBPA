#01_2345_5251

import random

def get_number_in_dials():
    a=0
    while a <= 3:
        x = input("How many dials should I generate in each lock combination?(Must be at least 3!)\n>")
        
        if (x.isdigit()):
            a = int(x)
        else:
            print("Please provide a valid number!\n")
            pass
            
        if (a<3):
            print("\nYou must provide a dial number greater than 3!\n\n\n")
        else:
            y = input("Please enter the number again to verify your choice.\n>")
            if (int(y)==a):
                return a
            else:
                print("\nThe numbers you have provided do not match! Please try again.")

def get_how_many_to_list():
    debounce = False
    while (debounce == False):
        x = input("How many lock combinations would you like?\n>")
        if (x.isdigit()):
            debounce = True
            return int(x)
        else:
            debounce = False
            print("Please provide a valid number!\n\n\n")
        
def get_number(min : int, max : int):
    return random.randrange(min, (max+1))

def next_combo_number(DIAL_NUMBER : int):
    ans = []
    i = 0
    while i < DIAL_NUMBER:
        ans.append(get_number(0,9))
        i+=1
    return ans
        
def print_answer(l : list):
    i = 0
    print("\n\n\n----------------\n")
    while i < len(l):
        a = ""
        for v in l[i]:
            a += str(v) + " "
        print("Number " + str(i+1) + ": " + a)
        i+=1
    print("\n" + str(len(l)) + " combinations were generated!")
    print("\n----------------\n")

def get_answer():
    a = get_number_in_dials()
    b = get_how_many_to_list()
    i = 0
    ans = [ ]
    while i < b:
        ans.append(next_combo_number(a))
        i+=1
    print_answer(ans)
    return ans

locks = get_answer()

# Final time with interuptions 44m55s18
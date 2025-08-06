import random

def Dice():
    print(random.randint(1,6))

while True:
    state = input("Wanna Roll (y/n)? : ").lower().strip()
    if(state == "y"):
        Dice()
    else:
        print("Thanks for playing!")
        break

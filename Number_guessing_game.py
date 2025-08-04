#Guess the NUmber according to ur difficulty Level

import random
def PlayGame():
    computer = random.randint(1,10)

    #Selection of difficulty level
    mode = input("Enter Your Difficutly Level as easy/hard : ").lower().strip()
    attempts = 5 if mode == "easy" else 3

    while(attempts > 0):
    
        user = int(input("Enter your Guess : "))

        if(user == computer):
            print("You Won!!")
            print(f"The number was {computer}!")
            break

        else:
            if(user > computer):
                print("Too High!")
            else:
                print("Too Low!")

        attempts -= 1

    if(attempts == 0):
        print("You Lose!")
        print(f"The number was {computer}!")

while True:
    PlayGame()
    again = input("You want to play again ? (yes/no) : ").lower().strip()
    if(again != "yes"):
        print("Thanks for playing!")
        break


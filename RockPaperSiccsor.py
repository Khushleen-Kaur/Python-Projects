import random as r

print("Game begains!! ROCK, PAPER, SCISSORS!!")
comp = r.randint(0,2)

for_comp = { 
    0 : "Rock",
    1 : "Paper",
    2 : "Scissor"
}

user = input("Enter your choice(Rock,Paper,Scissor) : ").capitalize().strip()
if(user == for_comp[comp]):
    print(f"Its a draw! Both did {for_comp[comp]}.")

elif(for_comp[comp]=="Rock" and user == "Paper"):
    print(f"You win! You did {user} and comp did {for_comp[comp]}.")

elif(for_comp[comp]=="Rock" and user=="Scissor"):
    print(f"You Loss! You did {user} and comp did {for_comp[comp]}.")

elif(for_comp[comp]=="Paper" and user == "Rock"):
    print(f"You Loss! You did {user} and comp did {for_comp[comp]}.")

elif(for_comp[comp]=="Paper" and user=="Scissor"):
    print(f"You win! You did {user} and comp did {for_comp[comp]}.")

elif(for_comp[comp]=="Scissor" and user == "Paper"):
    print(f"You Loss! You did {user} and comp did {for_comp[comp]}.")

elif(for_comp[comp]=="Scissor" and user=="Rock"):
    print(f"You win! You did {user} and comp did {for_comp[comp]}.")
    
else:
    print("Invalid Input! Try again.")


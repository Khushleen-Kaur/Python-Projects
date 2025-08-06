#How well you know me!

questions = [
    {
    "question":"What is my fav subject ?",
    "options":['A.Math','B.Physics','C.Chemistry','D.All of the above'],
    "answer":"A"
    },
    {
    "question":"What is my fav animal ?",
    "options":['A.Dogs','B.Cats','C.Pandas','D.None of the above'],
    "answer":"A"
    },
    {
    "question":"What is my fav color ?",
    "options":['A.Pink','B.Yellow','C.Black','D.White'],
    "answer":"C"
    },
    {
    "question":"What is my fav food?",
    "options":['A.Momos','B.Pizza','C.sandwitch','D.All of the above'],
    "answer":"D"
    },
    {
    "question":"What is my laptop brand ?",
    "options":['A.Lenovo','B.Asus','C.Apple','D.Hp'],
    "answer":"B"
    }

]

print("Game begains!")
score = 0

for ind,question in enumerate(questions):
    print(ind,question['question'])
    for i in question['options']:
        print(i,end="  ")
    ans = input("\nEnter answer(A/B/C/D) : ").upper().strip()
    if(ans == question['answer']):
        score += 1
        print("Correct answer!")
        print("Your score is",(score),"out of 5\n")
        
    else:
        print(f"Wrong answer! answer was {question['answer']}")
        print("Your score is",score,"out of 5\n")

print(f"Your final score is :",score)

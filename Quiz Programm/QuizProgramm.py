# dictionary that stores questions and answers
# have a variable that track the score of the player
# loop through the dictionary using the key values pairs\
# display each questions to the user and allow them to answer
# telling them wheather they are right or wrong
# showing the final result when quiz is completed

quiz = {
    "question1":{
        "question":"what is the capital of France?",
        "answer":"Paris"
    },
    "question2":{
        "question":"what is the capital of Germany?",
        "answer":"Berlin"
    },
    "question3":{
        "question":"what is the capital of Italy?",
        "answer":"Rome"
    },
    "question4":{
        "question":"what is the capital of Spain?",
        "answer":"Madrid"
    },
    "question5":{
        "question":"what is the capital of Portugal?",
        "answer":"Lisbon"
    },
    "question6":{
        "question":"what is the capital of Switzerland?",
        "answer":"Bern"
    },
    "question7":{
        "question":"what is the capital of Austria?",
        "answer":"Vienna"
    },
    "question8":{
        "question":"what is the capital of Uzbekistan?",
        "answer":"Tashkent"
    },
}

score =0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: \n")
    
    if answer.lower()==value['answer'].lower():
        print("Correct! Good Job!")
        score+=1
        print(f"Your score is {score}")
        print("")
    else:
        print("Incorrect! Let's try again next time!")
        print(f"Your score is {score}")
        print("")
  
def percentage_calculator():
    print(f"Your percentage rate score is {score/8 * 100} %") 
    
         
if score > 1:
    print(f"You got {score} questions correctly. Congratulations!")
    percentage_calculator()
elif score == 1:
    print("You have found only a single question correctly, never stop learning and never give up!")
    percentage_calculator()
else:
    print("Stupid, Dump Sheet! Bull Sheet, Fuck Yourself! ")
    percentage_calculator()
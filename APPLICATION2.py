print (" Welcome to the All-round Quiz Game")

questions = ( "Which river is the longest in the world?:",   
              "What is the capital of Japan?:")
             
            
options = (
    ("A. Amazon","B. Mississippi","C. Nile","D. Yangtze"),
    ("A. Beijing","B. Tokyo","C. Seoul","D. Bangkok"))
           
answers = ("C","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]}is the correct answer")
    question_num +=1
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!YOU'RE A GENIUS")
    else:
        print("INCORRECT!TRY HARDER")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------")
print("     RESULTS     ")
print("-----------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()          

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()          

score = int (score / len(questions) * 100)
print(f"Your score is: {score}%")
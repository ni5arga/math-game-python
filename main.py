import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*"])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def play_game():
    score = 0
    while True:
        question, answer = generate_question()
        user_answer = input(f"What is {question}? ")
        if user_answer == "quit":
            break
        elif user_answer.isdigit() and int(user_answer) == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        print(f"Score: {score}")
    print("Thanks for playing!")

play_game()

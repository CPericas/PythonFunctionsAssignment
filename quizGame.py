#Objective:
#The aim of this assignment is to create a quiz game that asks questions and checks answers.

#Task 1: Develop a list of questions and answers.
#Task 2: Write a function that quizzes the user and takes their answers.
#Task 3: Score the quiz and give the user feedback on their performance.

questions = [
    "What is 5 + 5?",
    "What is the opposite of 'South'?",
    "What is the largest state in the U.S.?",
    "What is 7 - 3?"
]
score = 0
answers = [10, 'north', 'alaska', 4]
answer_types = [int, str, str, int]
for i in range(len(questions)):
    user_answers = input(questions[i] + " ")
    if answer_types[i] == str:
        converted_answer = user_answers.lower()
    else:
        converted_answer = answer_types[i](user_answers)
    if converted_answer == answers[i]:
        print("Correct!")    
        score += 1
    else:
        print("Wrong answer.")
print(f"Your final score is {score}/{len(questions)}.")

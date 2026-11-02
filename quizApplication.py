
questions = [
    {
        "question": "1. Which language is used for Python programming?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "2. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. &"],
        "answer": "C"
    },
    {
        "question": "3. Which function is used to display output?",
        "options": ["A. input()", "B. print()", "C. output()", "D. show()"],
        "answer": "B"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["A. Integer", "B. String", "C. Float", "D. Boolean"],
        "answer": "D"
    },
    {
        "question": "5. Which loop is used to repeat statements?",
        "options": ["A. for", "B. if", "C. break", "D. return"],
        "answer": "A"
    }
]

score = 0

print("===== PYTHON QUIZ APPLICATION =====")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct Answer:", q["answer"])

print("\n===== QUIZ RESULT =====")
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)
print("Your Score:", score, "/", len(questions))

if score >= 3:
    print("Congratulations! You Passed.")
else:
    print("Better Luck Next Time!")


questions = {
    "which component is known as the brain of a computer?": "CPU",
    "which planet is known as the red planet?": "Mars",
    "Who developed the Python programming language?": "Guido van Rossum",
    "Which is the largest ocean in the world?": "Pacific Ocean",
    "Who is known as the Father of the Indian Constitution?": "Dr. B. R. Ambedkar",
    "Which gas do plants absorb during photosynthesis?":  "Carbon dioxide",
    "Who was the first President of India?": "Dr. Rajendra Prasad",
    "What is the capital of Australia?": "Canberra",
    "Which is the hardest natural substance?": "Diamond",
    "How many bits are there in one byte?": "8"
}

score = 0

for question, answer in questions.items():
    print(f"Question: {question}")

    user_answer = input("Your answer: ")

    if user_answer.lower() == answer.lower():
        score += 1
        print("Correct answer")
    else:
        print("Wrong answer")

print("QUIZ COMPLETED!")

percentage = round((score / len(questions)) * 100, 2)

print(f"Your score: {score}/{len(questions)}")
print(f"Percentage: {percentage}%")

if score == 10:
    print("Perfect Score!")
elif score >= 8:
    print("Good Job!")
elif score >= 5:
    print("Not Bad!")
else:
    print("Keep Practicing!")

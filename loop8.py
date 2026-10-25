# Mini project 8 : Quiz application
quiz_data = [
    {"question": "what is the capital of india ?": "New delhi"},
    {"question": "How many days are there in a normal year ?", "answer":"365"},
    {"question": "What is 5 multiplied by 6", "answer":"30"},
    {"question": "Which planet is known as the red planet?", "answer":"Mars"}
]
score = 0
print("--- Welcome to the Quizs! ---")
print("Note: Answer are case-sensitive , so type carefully.\n")

for item in quiz_data:
    print(item["question"])
    user_answer = input("Your answer: ")
    if user_answer.strip().lower() == item["answer"].lower():
        print("Correct!\n")
        score = score + 1
    else:
        print(f"Incorrect. The correct answer is : {item['answer']}\n")
total_question = len(quiz_data)
percentage = (score / total_question) * 100
if percentage >= 80:
   message = "Excellent"
elif percentage >= 60:
    message = "Good"
else:
    message = "Keep trying"
print("\n" + "="*20)
print("   QUIZ RESULTS   ")
print("\n" + "="*20)
print(f"Score:           {score} / {total_question}")
print(f"percentage:       {percentage}%")
print(f"Performance message:{message}")
print("\n" + "="*20)

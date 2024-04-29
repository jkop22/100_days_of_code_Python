from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

quiz_bank = []

start = int(input(f"How many questions do U wanna in the quiz? ({len(question_data)} max.): "))

for i in range(start):
    q_txt = question_data[i-1]["text"]
    q_ans = question_data[i-1]["answer"]
    q = Question(q_txt, q_ans)
    quiz_bank.append(q)

# for n in range(start):
#     print(quiz_bank[n].q_text, quiz_bank[n].answer)

quiz = QuizBrain(quiz_bank)
while quiz.still_has_questions():
    quiz.ask_question()

print("QUIZ DONE")
print(f"Your final score is: {quiz.score} / {len(quiz_bank)}. Bye")




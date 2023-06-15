from question import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    answer = question['answer']
    new_q = Question(question_text, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print(f"You completed the project!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

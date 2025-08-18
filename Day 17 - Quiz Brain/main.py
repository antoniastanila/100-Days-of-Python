from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for element in question_data:
    new_question = Question(element["question"], element["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(
    f"Congrats on finishing the quiz! Here's your final score: {quiz.score}/{quiz.question_number}")

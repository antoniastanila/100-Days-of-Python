class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        user_input = input(
            f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ").lower()

        self.check_answer(user_input, self.question_list[self.question_number])
        self.question_number += 1

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        return True

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is: {correct_answer.answer}.")
        print(
            f"Your current score is: {self.score}/{self.question_number + 1}")
        print("\n")

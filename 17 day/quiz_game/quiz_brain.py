class QuizBrain:
    def __init__(self, quiz_bank):
        self.q_num = 0
        self.quiz_bank = quiz_bank
        self.score = 0

    def still_has_questions(self):
        if self.q_num < len(self.quiz_bank):
            return True
        else:
            return False    

    def ask_question(self):
        curr_question = self.quiz_bank[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q.{self.q_num}: {curr_question.q_text} ('True' / 'False'): ")
        self.check_answer(user_answer, curr_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"Wrong answer ... correct was: {correct_answer}")
        print(f"Your current score is: {self.score} / {self.q_num}")
        print("\n")

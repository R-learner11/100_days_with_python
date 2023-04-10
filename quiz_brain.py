class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no} : {current_question.text} True/False?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you've got it right!")
            self.score += 1
        else:
            print("you're wrong")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_no}.\n")

    def final_score(self):
        print("You've completed the quiz.")
        print(f"Your final score is: {self.score}/{self.question_no}")


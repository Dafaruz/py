class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.quiz_list = q_list
        self.score = 0

    def next_question(self):

        current_question = self.quiz_list[self.q_num]
        self.q_num += 1
        user_ans = input(f"Q.{self.q_num}:  {current_question.txt} (True/False):")
        self.err_checker(user_ans, current_question)

    def end_of_question(self):
        return self.q_num < len(self.quiz_list)

    def err_checker(self, user_ans, current_question):

        if user_ans.lower() == current_question.answer.lower():
            self.score += 1
            print(f"Your are right your score is: {self.score}/{len(self.quiz_list)})")
        else:
            print(f"You are wrong the tight answer is : {current_question.answer}")
            print(f"Your score is: {self.score}/{len(self.quiz_list)})")

import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = q_list[0]

    def still_has_questions(self):
        return self.question_number < len(self.question_list)   # will return boolean

    def next_question(self):
        self.question_number += 1 # next question
        self.current_question = self.question_list[self.question_number]
        self.current_question.text = html.unescape(self.current_question.text)  # fix html code

        return f"Q.{self.question_number}: {self.current_question.text} (True/False):"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False



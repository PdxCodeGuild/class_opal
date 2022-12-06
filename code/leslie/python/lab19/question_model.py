class Question:
    def __init__(self, question, correct_answer, choices: list):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = choices

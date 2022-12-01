from question_model import Question


class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0  # will increment number to get next question
        self.score = 0
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):  # checks if quiz has more questions
        return self.question_number < len(self.questions)

    def next_question(self):
        '''gets question from questions list at index [question_number]
        increments question_number attribute'''
        self.current_question = self.questions[self.question_number]
        self.question_number += 1
        q_text = self.current_question.question_text
        return f"Question {self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        # checks user's answer against correct answer, adjusts score if correct
        # (need the 'type: ignore' below or else will get an error. This way, Pylance ignores it.)
        correct_answer = self.current_question.correct_answer  # type: ignore
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def get_score(self):
        # get number of correct answers, wrong answers, and score PERCENTAGE
        wrong = self.question_number - self.score
        score_percent = int(self.score / self.question_number * 100)
        return (self.score, wrong, score_percent)

    
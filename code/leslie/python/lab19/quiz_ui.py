from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain
from question_model import Question
import winsound


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()  # creates window
        self.window.title("Quiz App")  # creates window title
        self.window.geometry("850x530")  # creates window size
        self.window.configure(bg="LightCyan4")
        self.display_title()  # displays title
        self.window.attributes('-topmost', True)  # keeps window on top...
        # but doesn't force it to stay there
        self.window.after_idle(self.window.attributes, '-topmost', False)
        # self.window.overrideredirect(True)  # removes title bar

        # create canvas to display questions
        self.canvas = Canvas(width=800, height=250, bg='LightCyan4')
        self.question_text = self.canvas.create_text(
            400, 125, text="Question", width=680, font=('Gill Sans MT', 20, 'italic'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        '''StringVar stores value of user input. This one is for the
        user's answer.
        Syntax: tk.StringVar(container, value, name)

        container: widget StringVar object assoc. with. Default- root window
        value: initial value, default - empty string
        name: name given to defined variable, default -- PY_VARnum '''
        self.user_answer = StringVar()  # used in Radio buttons (73, 81)

        # display options with radio buttons
        self.opts = self.radio_buttons()
        self.display_options()

        # show whether answer is right or wrong
        self.feedback = Label(self.window, pady=10,
                              font=("Gill Sans MT", 15, "bold"), bg='LightCyan4')
        self.feedback.place(x=300, y=380)

        # next and quit button
        self.buttons()

        # mainloop
        self.window.mainloop()

    # displays title
    def display_title(self):
        title = Label(self.window, text="It's time for...Pickle Quiz!", width=40,
                      bg='#C48912', fg="linen", font=("Gill Sans Ultra Bold", 22))
        title.place(x=0, y=2)

    # displays question, itemconfig lets add text dynamically
    def display_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(
            self.question_text, text=q_text)

    def radio_buttons(self):  # to create radio buttons for options
        choice_list = []
        y_pos = 220  # set position of first option

    # add options to list
        while len(choice_list) < 4:
            radio_btn = Radiobutton(
                self.window, text="", variable=self.user_answer, value='', font=("Gill Sans MT", 18),  activebackground='LightCyan4', bg='LightCyan4')
            choice_list.append(radio_btn)  # add button to list
            radio_btn.place(x=200, y=y_pos)  # place the button
            y_pos += 40  # incrementing y-axis position by 40
        return choice_list  # returns buttons

    def display_options(self):  # display 4 options
        val = 0
        self.user_answer.set(None)  # type: ignore # deselects the options
        for option in self.quiz.current_question.choices:  # type: ignore
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):  # show feedback for each answer and keep checking for more questions
        # check if answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "yellow green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback['fg'] = 'tomato2'
            self.feedback['text'] = ('\u274E Oops! \n'
                                     f'The right answer is: {self.quiz.current_question.correct_answer}')  # type: ignore
        if self.quiz.has_more_questions():
            # moves to display next question and its options
            self.display_question()
            self.display_options()
        else:
            self.display_result()  # if there are no more questions, it displays score
            self.window.destroy()  # destroys self.window

    def buttons(self):  # show next & quit button
        next_button = Button(self.window, text="Next", command=self.next_btn,
                             width=10, bg="#88B370", fg="linen", font=("Gill Sans MT", 16, "bold"))
        next_button.place(x=350, y=460)  # places button on screen
        # making another button to quit
        quit_button = Button(self.window, text="Quit", command=self.window.destroy,
                             width=5, bg="#87BDD1", fg="linen", font=("Gill Sans MT", 16, "bold"))
        quit_button.place(x=700, y=50)

    def display_result(self):
        # displays result with messagebox
        correct, wrong, score_percent = self.quiz.get_score()
        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"
        # calculates percentage of correct answers
        result = f"Score: {score_percent}%"
        winsound.PlaySound("spanish-flea-herb-alpert22.wav",
                           winsound.SND_ASYNC)  # allows music to play at the same time as messagebox pop up
        if score_percent < 50:
            messagebox.showinfo(
                "Your results!", f"{result}\n\n{correct}\n\n{wrong}\n\nI'm not mad, I'm just disappointed.")
        elif score_percent >= 50 and score_percent <= 70:
            messagebox.showinfo(
                "Result", f"{result}\n\n{correct}\n\n{wrong}\n\nPretty good! You know some stuff!")
        elif score_percent >= 71 and score_percent <= 99:
            messagebox.showinfo(
                "Result", f"{result}\n\n{correct}\n\n{wrong}\n\nSomeone is wearing their smarty pants today! You know your stuff!")
        elif score_percent == 100:
            messagebox.showinfo(
                "Result", f"{result}\n\n{correct}\n\n{wrong}\n\nONE HUNDRED PERCENT! You are amazing. I'm OBSESSED with you. Call me.")

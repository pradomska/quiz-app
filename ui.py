from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_CANVAS = ("Arial", 18, "italic")
FONT_LABEL = ("Courier", 12, "normal")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score: 0", font=FONT_LABEL, fg="white", background=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, text="question", fill=THEME_COLOR, font=FONT_CANVAS, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.button_true = Button(image=true_img, relief="ridge", highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0)
        self.button_false = Button(image=false_img, relief="ridge", highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

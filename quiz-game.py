import tkinter as tk
from PIL import ImageTk, Image


class QuizGame(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Quiz Game")
        self.geometry("1620x1080")
        self.current_question = 0
        self.score = 0
        self.create_welcome_screen()

    def create_welcome_screen(self):
        outer_frame = tk.Frame(self, bg="black")
        outer_frame.pack(fill=tk.BOTH, expand=True)

        inner_frame = tk.Frame(outer_frame, bg="gray26", width=1000, height=100)
        inner_frame.pack(fill=tk.BOTH, expand=True, pady=(100, 200), padx=(100, 100))

        welcome_label = tk.Label(inner_frame, text="Welcome to the Astronomy Quiz", font=('times 32 underline'), bg="gray26",
                                 fg="white")
        welcome_label.pack(pady=100)

        rules_label = tk.Label(inner_frame, text="Rules:", font=('times 28 underline'), bg="gray26", fg="white", anchor=tk.W)
        rules_label.pack(fill=tk.X, padx=80)
        rules_label.place(x=350, y=200)

        rules_text = (
            "1. You will be presented with a number of multiple-choice questions.\n"
            "2. There is only one correct option.\n"
            "3. Your score will be calculated based on the correct answers.\n"
            "4. There is NO negative Marking. \n"
        )
        rules_info_label = tk.Label(inner_frame, text=rules_text, font=("times", 20), bg="gray26", fg="white",
                                    justify=tk.LEFT)
        rules_info_label.pack(fill=tk.X, padx=50)
        start_button = tk.Button(inner_frame, text="Start Quiz", font=("times", 24), bg="gray26", fg="white",
                                 command=self.start_quiz)
        start_button.pack()

    def start_quiz(self):
        for widget in self.winfo_children():  # Destroy all widgets in the current window
            widget.destroy()
        self.geometry("1600x720")

        self.questions = [
            {
                "question": "What is the closest star to Earth?",
                "options": ["A:Alpha Centauri", "B:Proxima Centauri", "C:Betelgeuse", "D:Sirius"],
                "answer": "A:Alpha Centauri"
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "options": ["A:Mars", "B:Venus", "C:Jupiter", "D:Saturn"],
                "answer": "A:Mars"
            },
            {
                "question": "What is the name of our galaxy?",
                "options": ["A:Andromeda", "B:Milky Way", "C:Sombrero", "D:Pinwheel"],
                "answer": "B:Milky Way"
            },
            {
                "question": "What causes the phases of the moon?",
                "options": ["A:Earth's shadow", "B:Gravitational pull", "C:Sunlight", "D:Planetary alignment"],
                "answer": "C:Sunlight"
            }
        ]

        self.create_widgets()
        self.show_question()

    def create_widgets(self):

        outer_frame = tk.Frame(self, bg="black")
        outer_frame.pack(fill=tk.BOTH, expand=True)

        inner_frame = tk.Frame(outer_frame, bg="gray26")
        inner_frame.pack(fill=tk.BOTH, side="left", pady=(100, 50), padx=(200, 0))

        self.questions_frame = tk.Frame(inner_frame, bg="gray26", width=100, height=50)
        self.questions_frame.pack(pady=20)

        self.question_number_label = tk.Label(inner_frame, font=("times", 32), bg="gray26", fg="white", width=15,
                                              height=1)
        self.question_number_label.pack(anchor=tk.W, padx=50)

        self.question_label = tk.Label(inner_frame, text="", font=("times", 26), bg="gray26", fg="white", width=35,
                                       height=1)
        self.question_label.pack(anchor=tk.W, padx=5, pady=30)

        self.var_answer = tk.StringVar()

        self.options_frame = tk.Frame(outer_frame, bg="gray26")
        self.options_frame.pack(fill=tk.BOTH, side="left", padx=(0, 200), pady=(100, 50))

        self.option_buttons = []
        for i in range(4):
            option_button = tk.Button(self.options_frame, font=("times", 24), width=30, fg="white", bg="gray26",
                                      borderwidth=5, relief="solid", command=lambda idx=i: self.select_option(idx))
            option_button.pack(pady=(50, 10), padx=50)
            self.option_buttons.append(option_button)

        self.feedback_label = tk.Label(inner_frame, text="", font=("times", 32), bg="gray26", fg="white")
        self.feedback_label.pack()

        self.finish_button = tk.Button(self.feedback_label, text="Finish", font=("times", 24), bg="gray26",
                                       fg="white", command=self.finish_quiz)
        self.finish_button.place(x=900, y=800)

    def show_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])

            question_number_text = f"Question {self.current_question + 1}/{len(self.questions)}"
            self.question_number_label.config(text=question_number_text)

        else:
            self.finish_button.pack()

    def select_option(self, selected_index):
        selected_option = self.questions[self.current_question]["options"][selected_index]
        correct_answer = self.questions[self.current_question]["answer"]

        if selected_option == correct_answer:
            self.score += 1

        self.current_question += 1

        if self.current_question == len(self.questions):
            self.show_results()
        else:
            self.show_question()

    def finish_quiz(self):
        destroy()

    def show_results(self):

        self.question_label.config(text="Quiz Completed!", width=50, font=("times", 32))
        self.options_frame.destroy()
        self.question_number_label.destroy()

        result_text = f"You scored {self.score} out of {len(self.questions)}"
        self.feedback_label.config(text=result_text)


if __name__ == "__main__":
    app = QuizGame()
    app.mainloop()

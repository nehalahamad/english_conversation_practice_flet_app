import flet as ft
import json
import random
import asyncio


class TimerProgressBar(ft.ProgressBar):
    def __init__(self, my_theme_color, page, next_question):
        super().__init__()
        self.page = page
        self.color = my_theme_color
        self.height = 1
        self.seconds = 10
        self.next_question = next_question

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_timer)

    def will_unmount(self):
        self.running = False

    async def update_timer(self):
        while self.seconds and self.running:
            # mins, secs = divmod(self.seconds, 60)
            # self.value = "{:02d}:{:02d}".format(mins, secs)
            self.value = (31-self.seconds)/30
            # self.page.update()
            self.page.views[-1].update()
            await asyncio.sleep(1)
            self.seconds -= 1
            def f1():
                pass
        self.next_question(ft.ControlEvent(name='click', data=None, target='_54',page=self.page, control=MyOutlinedButton('next', 'red', f1)))


class Question:
    def __init__(self, question):
        self.question = question

    def display(self, page):
        pass

    def get_answer(self):
        return None

class MCQQuestion(Question):
    def __init__(self, question, page:ft.Page, my_theme_color, next_question=None):
        super().__init__(question)
        self.page = page
        self.selected_option = None
        self.my_theme_color = my_theme_color
        # self.next_question = next_question

    def display(self, page, options):
        column = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
        column.controls.append(ft.Divider(color=self.my_theme_color)) ##########################
        # column.controls.append(TimerProgressBar(self.my_theme_color, self.page, self.next_question))


        for key, option in options.items():
            column.controls.append(ft.Row(
                controls=[
                    ft.Radio(value=option, width=30),
                    ft.Text(option, text_align=ft.TextAlign.LEFT, 
                        no_wrap=False,
                        width=self.page.window.width-90,
                    )
                ],
                spacing=0
            ))
            column.controls.append(ft.Divider(color=self.my_theme_color))

        # Create a RadioGroup with an on_change callback to update selected_option
        self.radio_group = ft.RadioGroup(
            content=column,
            on_change=lambda e: setattr(self, "selected_option", e.control.value)
        )
        # Add radio buttons for each option
        return ft.Container(
            content=self.radio_group,
            padding=10,
            margin=5,
            border_radius=5,
            expand=True,
            bgcolor=ft.Colors.WHITE,
            width=self.page.window.width
        )

    def get_answer(self):
        return self.selected_option

class TrueFalseQuestion(Question):
    def __init__(self, question):
        super().__init__(question)
        self.selected_option = None
        self.radio_group = None

    def display(self, page):
        column = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
        # Create a RadioGroup with an on_change callback for True/False options
        self.radio_group = ft.RadioGroup(
            content=column,
            on_change=lambda e: setattr(self, "selected_option", e.control.value)
        )
        self.radio_group.content.controls = [
            ft.Radio(value="True", label="True"),
            ft.Radio(value="False", label="False")
        ]
        return ft.Container(
            content=self.radio_group,
            border=ft.border.all(1, ft.Colors.BLACK),
            padding=10,
            margin=5,
            border_radius=5
        )

    def get_answer(self):
        return self.selected_option

class ShortAnswerQuestion(Question):
    def __init__(self, question):
        super().__init__(question)
        self.text_field = None

    def display(self, page):
        # Create a TextField for short answers and store it
        self.text_field = ft.TextField(text_align=ft.TextAlign.CENTER)
        return self.text_field

    def get_answer(self):
        return self.text_field.value if self.text_field else ""

class MyOutlinedButton(ft.OutlinedButton):
    def __init__(self, text, my_theme_color, on_click):
        super().__init__()
        self.text = text
        self.on_click = on_click
        self.my_theme_color = my_theme_color
        self.style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            side=ft.BorderSide(width=1, color=self.my_theme_color),
        )
        self.width=125

class QuizView(ft.View):
    def __init__(self, page: ft.Page, file_path:str, my_theme_color):
        super().__init__()
        self.route = "/quiz"
        self.page = page
        self.scroll = True
        self.horizontal_alignment = 'center'
        self.my_theme_color = my_theme_color

        self.current_question: int = 0
        self.score: int = 0
        self.selected_answers: list = []
        self.num_questions: int = 5

        self.appbar = ft.AppBar(
            title=ft.Text('Quizz', size=15),
            center_title=False,
            bgcolor=self.my_theme_color,
        )

        # Load questions once and sample a fixed set for the quiz
        with open(file_path, 'r') as file:
            self.questions_json = json.load(file)

        self.questions: list = random.sample(self.questions_json, self.num_questions)

        self.current_question_widget = None

        # ==================== Question ======================
        self.question_ref = ft.Ref[ft.Text]()
        self.question_label_ref = ft.Ref[ft.Text]()
        self.question_text = ft.Stack(
            controls=[
                ft.Container(
                    content=ft.Text(text_align=ft.TextAlign.LEFT, no_wrap=False, max_lines=5, width=self.page.width, size=15, ref=self.question_ref),
                    padding=10,
                    margin=ft.margin.only(left=5, right=5, top=12, bottom=5),
                    border_radius=5,
                    border=ft.border.all(1, self.my_theme_color),
                    bgcolor=ft.Colors.WHITE,
                ),
                ft.Container(
                    content=ft.Text(size=12, weight=ft.FontWeight.BOLD, ref=self.question_label_ref),
                    margin=ft.margin.only(left=15),
                    padding=ft.padding.only(left=5, right=5, bottom=3),
                    border_radius=5,
                    border=ft.border.all(1, self.my_theme_color),
                    bgcolor=ft.Colors.WHITE,
                )
            ]
        )
        # ==================== Options =======================
        self.options = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
        
        # ============ Prev and Nest buttons =================
        self.button_row = ft.Row(
            controls=[
                MyOutlinedButton("Prev", self.my_theme_color, on_click=self.prev_question), 
                MyOutlinedButton("Next", self.my_theme_color, on_click=self.next_question)
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        )
        # Adding question, option control and prev, next buttons to View
        self.controls.append(
            ft.Column(
                controls=[
                    self.question_text,
                    self.options,
                    self.button_row
                ], 
                alignment=ft.MainAxisAlignment.CENTER, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        self.load_question()

    def load_question(self):
        self.options.controls.clear()
        
        # Get the current question from the pre-sampled list
        question = self.questions[self.current_question]
        self.question_ref.current.value = question["question"]
        self.question_label_ref.current.value = f'Question: {self.current_question+1}'
        
        q_type = question["type"]
        if q_type == "mcq":
            q = MCQQuestion(question["question"], self.page, self.my_theme_color)
            # q = MCQQuestion(question["question"], self.page, self.my_theme_color, self.next_question)
            widget = q.display(self.page, question["options"])
            self.options.controls.append(widget)
            self.current_question_widget = q
        elif q_type == "true_false":
            q = TrueFalseQuestion(question["question"])
            widget = q.display(self.page)
            self.options.controls.append(widget)
            self.current_question_widget = q

        self.page.update()
    
    def next_question(self, e):
        # Capture the answer using the question widget's get_answer method
        user_answer: str = self.current_question_widget.get_answer() if self.current_question_widget else None
        correct_answer: str = self.questions[self.current_question]["answer"]
        explanation: str = self.questions[self.current_question].get("explanation", "")
        
        # Update score if the answer is correct
        if user_answer is not None and user_answer == correct_answer:
            self.score += 1
        
        self.selected_answers.append({
            "question": self.questions[self.current_question]["question"],
            "selected": user_answer if user_answer is not None else "",
            "correct": correct_answer,
            "explanation": explanation
        })
        
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
        else:
            self.show_results()
    
    def show_results(self):
        self.controls.clear()
        self.controls.append(
            ft.Text(f"Quiz Completed! Your score: {self.score}/{self.num_questions}", text_align=ft.TextAlign.CENTER)
        )
        for result in self.selected_answers:
            answer_match: bool = result['selected']==result['correct']
            self.controls.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Text(f"{result['question']}", width=self.page.width),
                                border=ft.border.all(1, self.my_theme_color),
                                border_radius=5,
                                padding=5,
                            ),
                            ft.Text(f"Your Answer: {result['selected']}", color=ft.Colors.BLUE),
                            ft.Text(f"Correct Answer: {result['correct']}", color=ft.Colors.GREEN) if not answer_match else ft.Container(),
                            ft.Container(
                                content=ft.Text(f"{result['explanation']}", size=12),
                                border=ft.border.all(1, self.my_theme_color),
                                border_radius=5,
                                padding=5,
                            )
                        ],
                        scroll=True
                    ),
                    border=ft.border.all(1, self.my_theme_color),
                    padding=5,
                    margin=5,
                    border_radius=5,
                    bgcolor=["#FDEFEF", "#EFFDEF"][answer_match] #['red', 'green']
                )
            )
        self.try_again_button = MyOutlinedButton("Try Again", self.my_theme_color, on_click=self.try_again)
        self.controls.append(self.try_again_button)
        self.update()
    
    def prev_question(self, e):
        if len(self.selected_answers) > 0:
            self.selected_answers.pop()
        if self.current_question > 0:
            self.current_question -= 1
            self.load_question()
    
    def try_again(self, e):
        self.current_question = 0
        self.score = 0
        self.selected_answers = []
        self.controls.clear()
        self.controls.append(
            ft.Column([
                self.question_text,
                self.options,
                self.button_row
            ], 
            alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        # Resample questions for a new quiz session
        self.questions = random.sample(self.questions_json, self.num_questions)
        self.load_question()
        self.page.update()

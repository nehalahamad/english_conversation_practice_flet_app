import flet as ft
import json
import random

ft.TextStyle()


class Question:
    def __init__(self, question):
        self.question = question

    def display(self, page):
        pass

    def get_answer(self):
        return None

class MCQQuestion(Question):
    def __init__(self, question, page:ft.Page):
        super().__init__(question)
        self.page = page
        self.selected_option = None
        self.radio_group = None

    def display(self, page, options):
        column = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
        for key, option in options.items():
            column.controls.append(ft.Row(
                controls=[
                    ft.Radio(value=option),
                    ft.Container(
                        content=ft.Text(option, text_align=ft.TextAlign.LEFT, 
                            no_wrap=False,
                            max_lines=5,
                            width=self.page.width
                        ),
                        padding=10,
                        margin=5,
                        border_radius=5,
                        bgcolor=ft.Colors.PINK_100,
                        width=300
                    )
                ],
                # width=360,
                spacing=0
            )
            )

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
            width=360
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

class QuizView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/quiz"
        self.page = page
        self.scroll = True
        self.horizontal_alignment = 'center'


        self.current_question = 0
        self.score = 0
        self.selected_answers = []
        self.num_questions = 10

        self.appbar = ft.AppBar(
            title=ft.Text('Quizz', size=15),
            center_title=False,
            bgcolor='#06b7bd',
            actions=[
                ft.IconButton(ft.Icons.HOME, on_click=lambda e: e.page.go('/')),
            ]
        )

        # Load questions once and sample a fixed set for the quiz
        # self.questions_json = json.load(open('src/assets/questions.json', 'r'))
        file_path = "src/assets/docker_question_new.json"
        with open(file_path, 'r') as file:
            self.questions_json = json.load(file)

        self.questions = random.sample(self.questions_json, self.num_questions)
        # print(self.questions_json[0]["options"])

        self.current_question_widget = None

        self.question_text = ft.Container(
            content=ft.Text(
                text_align=ft.TextAlign.LEFT, 
                no_wrap=False,
                max_lines=5,
                width=self.page.width
            ),
            padding=10,
            margin=5,
            border_radius=5,
            bgcolor=ft.Colors.WHITE
        )
        self.feedback = ft.Text(color=ft.Colors.GREEN, text_align=ft.TextAlign.CENTER)
        self.options = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
        self.answer_input = None
        self.try_again_button = ft.ElevatedButton("Try Again", on_click=self.try_again)
        
        self.button_row = ft.Row(
            [
                ft.ElevatedButton("Prev", on_click=self.prev_question), 
                ft.ElevatedButton("Next", on_click=self.next_question)
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.controls.append(
            ft.Column([
                self.question_text,
                self.options,
                self.feedback,
                self.button_row
            ], 
            alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        self.load_question()

    def load_question(self):
        self.feedback.value = ""
        self.options.controls.clear()
        if self.answer_input:
            try:
                self.controls.remove(self.answer_input)
            except Exception:
                pass
            self.answer_input = None
        
        # Get the current question from the pre-sampled list
        question = self.questions[self.current_question]
        self.question_text.content.value = question["question"]
        
        q_type = question["type"]
        if q_type == "mcq":
            q = MCQQuestion(question["question"], self.page)
            widget = q.display(self.page, question["options"])
            self.options.controls.append(widget)
            self.current_question_widget = q
        elif q_type == "true_false":
            q = TrueFalseQuestion(question["question"])
            widget = q.display(self.page)
            self.options.controls.append(widget)
            self.current_question_widget = q
        elif q_type == "short":
            q = ShortAnswerQuestion(question["question"])
            self.answer_input = q.display(self.page)
            self.controls.append(self.answer_input)
            self.current_question_widget = q

        self.page.update()
    
    def next_question(self, e):
        # Capture the answer using the question widget's get_answer method
        user_answer = self.current_question_widget.get_answer() if self.current_question_widget else None
        correct_answer = self.questions[self.current_question]["answer"]
        explanation = self.questions[self.current_question].get("explanation", "")
        print(user_answer, '=== ', correct_answer)
        
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
            ft.Text(f"Quiz Completed! Your score: {self.score}/{len(self.questions)}", text_align=ft.TextAlign.CENTER)
        )
        for result in self.selected_answers:
            self.controls.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(f"Question: {result['question']}"),
                            ft.Text(f"Your Answer: {result['selected']}", color=ft.Colors.RED),
                            ft.Text(f"Correct Answer: {result['correct']}", color=ft.Colors.GREEN),
                            ft.Text(f"Explanation: {result['explanation']}")
                        ],
                        scroll=True
                    ),
                    border=ft.border.all(1, ft.Colors.BLACK),
                    padding=10,
                    margin=5,
                    border_radius=5
                )
            )
        self.controls.append(self.try_again_button)
        self.update()
        # self.page.update()
    
    def prev_question(self, e):
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
                self.feedback,
                self.button_row
            ], 
            alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        # Resample questions for a new quiz session
        self.questions = random.sample(self.questions_json, self.num_questions)
        self.load_question()
        self.page.update()

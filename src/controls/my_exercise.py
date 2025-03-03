import flet as ft
from controls.my_text import MyText

class EContainer(ft.Container):
    def __init__(self, etext, color=ft.Colors.BLUE):
        super().__init__()
        self.content=MyText(etext, size=15, color=color)
        self.bgcolor=ft.Colors.WHITE
        self.border_radius=5
        self.padding=5

class TContainer(ft.Container):
    def __init__(self, ttext, bgcolor='white'):
        super().__init__()
        self.content=MyText(ttext, size=18)
        self.bgcolor=bgcolor
        self.padding=10
        self.border_radius=10
        self.alignment=ft.alignment.center


class Exercise:
    def __init__(self):
        self.conversation_font_size = 15

    def display(self, exercise):
        title = TContainer(exercise["title"], '#3de5eb')
        example_sentence = TContainer(exercise["example_sentence"], '#69f5fa')

        column = ft.Column(expand=2, scroll=True)
        for line in exercise["lines"]:
            column.controls.append(
                ft.Container(
                    content=EContainer(line['word'], ft.Colors.BLUE),
                    alignment=ft.alignment.center_left,
                )
            )
            column.controls.append(
                ft.Container(
                    content=EContainer(line['sentence'], ft.Colors.RED),
                    alignment=ft.alignment.center_right,
                    
                )
            )
        return ft.Column(
            controls=[
                title,
                example_sentence,
                column
            ],
        )

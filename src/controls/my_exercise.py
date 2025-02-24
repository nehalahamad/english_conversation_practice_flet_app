import flet as ft
from controls.my_text import MyText

class Exercise:
    def __init__(self):
        self.conversation_font_size = 15

    def display(self, exercise):
        title = ft.Container(
            content=MyText(exercise["title"], size=18),
            bgcolor='#3de5eb',
            padding=10,
            # margin=5,
            border_radius=10,
            # expand=True,
            alignment=ft.alignment.center
        )
        example_sentence = ft.Container(
            content=MyText(exercise["example_sentence"], size=18),
            bgcolor='#69f5fa',
            padding=10,
            # margin=5,
            border_radius=10,
            # expand=True,
            alignment=ft.alignment.center
        )

        column = ft.Column(
            expand=2,
            scroll=True

        )
        for line in exercise["lines"]:
            word = line['word']
            sentence = line['sentence']
            column.controls.append(
                ft.Container(
                    content=ft.Container(
                        content=MyText(word, size=self.conversation_font_size, color=ft.Colors.BLUE),
                        bgcolor=ft.Colors.WHITE,
                        # alignment=ft.alignment.center_left,
                        border_radius=ft.border_radius.only(top_right=10, bottom_right=10),
                        padding=5
                    ),
                    alignment=ft.alignment.center_left,
                )
            )
            column.controls.append(
                ft.Container(
                    content=ft.Container(
                        content=MyText(sentence, size=self.conversation_font_size, color=ft.Colors.RED),
                        bgcolor=ft.Colors.WHITE,
                        alignment=ft.alignment.center_right,
                        border_radius=ft.border_radius.only(top_left=5, bottom_left=5),
                        padding=5
                    ),
                    
                )
            )
        return ft.Column(
            controls=[
                title,
                example_sentence,
                column
            ],
            # scroll=True
        )

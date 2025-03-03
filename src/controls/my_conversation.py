import flet as ft
from controls.my_text import MyText


class CContainer(ft.Container):
    def __init__(self, line, color=ft.Colors.BLUE):
        super().__init__()
        self.bgcolor=ft.Colors.WHITE
        self.border_radius=5
        self.padding=5
        self.content=MyText(line, size=15, color=color, selectable=True)


class Conversation:
    def __init__(self):
        self.conversation_font_size = 15

    def display(self, conversation):
        title = ft.Container(
            content=MyText(conversation["title"], size=18, selectable=True),
            bgcolor='#3de5eb',
            padding=10,
            margin=5,
            border_radius=10,
            # width=360,
            alignment=ft.alignment.center
        )

        column = ft.Column()

        for line in conversation["lines"]:
            if 'S1.' in line:
                line = line.split('S1.')[1].strip()
                column.controls.append(
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                CContainer(line, ft.Colors.BLUE),
                            ],
                            wrap=True,
                        ),
                        alignment=ft.alignment.center_left
                    )
                )
            elif 'S2.' in line:
                line = line.split('S2.')[1].strip()
                column.controls.append(
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                CContainer(line, ft.Colors.RED),
                                ft.Icon(name=ft.Icons.FACE_4),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                            wrap=True,
                    
                        ),
                        alignment=ft.alignment.center_right,
                    )
                )
        
        return ft.Column(
            # alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                title,
                column
            ]
        )
   
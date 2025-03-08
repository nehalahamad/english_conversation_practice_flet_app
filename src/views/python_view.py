import flet as ft


class PythonView(ft.View):
    def __init__(self, page:ft.Page, my_theme_color):
        super().__init__()
        self.route = "/python_quiz_list"
        self.page = page
        self.scroll = True
        self.horizontal_alignment = 'center'
        self.my_theme_color = my_theme_color

        self.appbar = ft.AppBar(
            title=ft.Text('Python', size=15),
            center_title=False,
            bgcolor=self.my_theme_color,
        )

        self.controls.append(
            ft.ListView(
                controls=[
                    ft.TextButton('Regular Expression', on_click=lambda _: page.go("/python_regex_quiz"))
                ]
            )
        )
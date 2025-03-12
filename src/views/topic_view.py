import flet as ft
from typing import List, Dict

class TopicView(ft.View):
    def __init__(self, page:ft.Page, my_theme_color, topics: List[Dict]):
        super().__init__()
        self.route = "/quiz_list"
        self.page = page
        self.scroll = True
        self.horizontal_alignment = 'center'
        self.my_theme_color = my_theme_color

        self.appbar = ft.AppBar(
            title=ft.Text('Topics', size=15),
            center_title=False,
            bgcolor=self.my_theme_color,
        )

        for topic in topics:

            self.controls.append(
                ft.ListView(
                    controls=[
                        ft.TextButton(topic["topic_name"], on_click=lambda _: page.go(topic["topic_route"]))
                    ]
                )
            )
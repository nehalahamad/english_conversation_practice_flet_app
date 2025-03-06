import flet as ft
# from navigation_card import NavigationCard

class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/",
            controls=[
                ft.AppBar(title=ft.Text("Home"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                ft.ListView(
                    controls=[
                        ft.ListTile(
                            title=ft.Text("English Conversation Practice"), 
                            leading=ft.Image(src="icons8-english-48.png", width=40, height=40, border_radius=50),
                            on_click=lambda _: page.go("/ecp")
                        ),

                        ft.ListTile(
                            title=ft.Text("Docker"), 
                            leading=ft.Image(src="docker.png", width=40, height=40, border_radius=50),
                            trailing=ft.IconButton(ft.Icons.QUIZ_ROUNDED, on_click=lambda _: page.go("/quiz")),
                            on_click=lambda _: page.go("/docker")
                        ),
                
                    ],
                    
                )
            ]
        )


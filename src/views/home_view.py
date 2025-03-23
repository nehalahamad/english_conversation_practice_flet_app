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
                            leading=ft.Image(src="icons/icons8-english-48.png", width=40, height=40, border_radius=50),
                            on_click=lambda _: page.go("/ecp")
                        ),

                        ft.ListTile(
                            title=ft.Text("Docker"), 
                            leading=ft.Image(src="icons/docker.png", width=40, height=40, border_radius=50),
                            on_click=lambda _: page.go("/docker"),
                            trailing=ft.IconButton(ft.Icons.QUIZ_ROUNDED, on_click=lambda _: page.go("/docker_quiz")),
                        ),
                        ft.ListTile(
                            title=ft.Text("Kubernetes"), 
                            leading=ft.Image(src="icons/icons8-kubernetes-48.png", width=40, height=40, border_radius=50),
                            # on_click=lambda _: page.go("/docker"),
                            trailing=ft.IconButton(ft.Icons.QUIZ_ROUNDED, on_click=lambda _: page.go("/kubernetes_quiz")),
                        ),
                        ft.ListTile(
                            title=ft.Text("Git"), 
                            leading=ft.Image(src="icons/icons8-git-48.png", width=40, height=40, border_radius=50),
                            on_click=lambda _: page.go("/git"),
                            trailing=ft.IconButton(ft.Icons.QUIZ_ROUNDED, on_click=lambda _: page.go("/git_quiz")),
                        ),
                        ft.ListTile(
                            title=ft.Text("Python"), 
                            leading=ft.Image(src="icons/icons8-python-48.png", width=40, height=40, border_radius=50),
                            # on_click=lambda _: page.go("/docker"),
                            trailing=ft.IconButton(ft.Icons.QUIZ_ROUNDED, on_click=lambda _: page.go("/python_quiz_list")),
                        ),
                        ft.ListTile(
                            title=ft.Text("MongoDB"), 
                            leading=ft.Image(src="icons/icons8-mongo-db-48.png", width=40, height=40, border_radius=50),
                            # on_click=lambda _: page.go("/docker"),
                            trailing=ft.IconButton(ft.Icons.QUIZ_ROUNDED, on_click=lambda _: page.go("/mongodb_quiz_list")),
                        ),
                        ft.ListTile(
                            title=ft.Text("Linux"), 
                            leading=ft.Image(src="icons/icons8-linux-64.png", width=40, height=40, border_radius=50),
                            # on_click=lambda _: page.go("/docker"),
                            trailing=ft.IconButton(ft.Icons.QUIZ_ROUNDED, on_click=lambda _: page.go("/linux_quiz_list")),
                        ),
                
                    ],
                    
                )
            ]
        )


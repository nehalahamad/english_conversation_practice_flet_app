import flet as ft
# from navigation_card import NavigationCard

class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/",
            controls=[
                ft.AppBar(title=ft.Text("Home"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                ft.ElevatedButton("Go ECP", on_click=lambda _: page.go("/ecp"))
            ]
        )

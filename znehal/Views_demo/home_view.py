import flet as ft
from navigation_card import NavigationCard

class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/",
            controls=[
                ft.AppBar(title=ft.Text("Home"), bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST),
                ft.Column(
                    [
                        NavigationCard("Store", "Visit the store page.", "/store", page)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                )
            ]
        )

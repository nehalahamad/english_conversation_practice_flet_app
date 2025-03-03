import flet as ft
from navigation_card import NavigationCard

class StoreView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/store",
            controls=[
                ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST),
                ft.Column(
                    [
                        NavigationCard("Home", "Return to the home page.", "/", page)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                )
            ]
        )

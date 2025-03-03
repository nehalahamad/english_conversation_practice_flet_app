import flet as ft

class NavigationCard(ft.Card):
    def __init__(self, title: str, description: str, route: str, page: ft.Page):
        super().__init__()
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, weight=ft.FontWeight.BOLD, size=18),
                    ft.Text(description, size=14, color=ft.colors.GREY),
                    ft.ElevatedButton(f"Go to {title}", on_click=lambda _: page.go(route))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            padding=15,
            margin=10,
            # bgcolor=ft.colors.SURFACE_VARIANT,
            border_radius=10
        )

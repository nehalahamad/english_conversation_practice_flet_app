import flet as ft
from home_view import HomeView
from store_view import StoreView

class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Flet Routes Example"
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.route_change(self.page.route)  # Load initial view

    def route_change(self, route):
        """Handles route changes and updates views dynamically."""
        self.page.views.clear()

        if route == "/store":
            self.page.views.append(StoreView(self.page))
        else:  # Default to home
            self.page.views.append(HomeView(self.page))

        self.page.update()

    def view_pop(self, view):
        """Handles back navigation."""
        if len(self.page.views) > 1:
            self.page.views.pop()
            self.page.go(self.page.views[-1].route)

def main(page: ft.Page):
    MyApp(page)  # Create an instance of MyApp

ft.app(main, view=ft.AppView.WEB_BROWSER)

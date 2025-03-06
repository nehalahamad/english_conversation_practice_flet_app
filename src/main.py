import flet as ft
from views.ecp_view import ECPView
from views.docker_view import DockerView
from views.quiz_view import QuizView
from views.home_view import HomeView

class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.width = 360
        self.page.scroll=True
        self.page.title = "Flet Routes Example"
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.route_change(self.page.route)  # Load initial view

    def route_change(self, route):
        """Handles route changes and updates views dynamically."""
        self.page.views.clear()

        if self.page.route == "/":  # Default to home
            self.page.views.append(HomeView(self.page))
        elif self.page.route == "/ecp":
            self.page.views.append(ECPView(self.page))
        elif self.page.route == "/docker":
            self.page.views.append(DockerView(self.page))
        elif self.page.route == "/quiz":
            self.page.views.append(QuizView(self.page))

        self.page.update()

    def view_pop(self, view):
        """Handles back navigation."""
        if len(self.page.views) > 1:
            self.page.views.pop()
            self.page.go(self.page.views[-1].route)

def main(page: ft.Page):
    MyApp(page)  # Create an instance of MyApp

# ft.app(main, view=ft.AppView.WEB_BROWSER)
ft.app(main, assets_dir="assets")

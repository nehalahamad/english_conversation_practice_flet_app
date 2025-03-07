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
        self.page.title = "Nehal Ahmad App"
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.route_change(self.page.route)  # Load initial view

    def route_change(self, route):
        """Handles route changes and updates views dynamically."""

        if self.page.route == "/":  # Default to home
            self.page.views.clear()
            self.page.views.append(HomeView(self.page))

        elif self.page.route == "/ecp":
            self.page.views.clear()
            self.page.views.append(ECPView(self.page))

        elif self.page.route == "/docker":
            self.page.views.append(DockerView(self.page))

        elif self.page.route == "/docker_quiz":
            file_path = "src/assets/docker_question_new.json"
            my_theme_color = '#06b7bd'
            self.page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN,)
            self.page.views.append(QuizView(self.page, file_path, my_theme_color))

        elif self.page.route == "/kubernetes_quiz":
            file_path = "src/assets/kubernetes_question_new.json"
            my_theme_color = 'blue'
            self.page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE,)
            self.page.views.append(QuizView(self.page, file_path, my_theme_color))

        elif self.page.route == "/git_quiz":
            file_path = "src/assets/git_question_new.json"
            my_theme_color = '#FF6600'
            self.page.theme = ft.Theme(color_scheme_seed=ft.Colors.ORANGE,)
            self.page.views.append(QuizView(self.page, file_path, my_theme_color))

        self.page.update()

    def view_pop(self, view):
        """Handles back navigation."""
        if len(self.page.views) > 1:
            self.page.views.pop()
            self.page.go(self.page.views[-1].route)
            self.page.update()

def main(page: ft.Page):
    MyApp(page)  # Create an instance of MyApp

# ft.app(main, view=ft.AppView.WEB_BROWSER)
ft.app(main, assets_dir="assets")

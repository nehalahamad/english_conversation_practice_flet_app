import flet as ft
from views.ecp_view import ECPView
from views.docker_view import DockerView
from views.git_commands import GitView
from views.quiz_view import QuizView
from views.home_view import HomeView
from views.topic_view import TopicView

class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.width = 360
        self.page.scroll=True
        self.page.title = "Nehal Ahamad App"
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

        elif self.page.route == "/git":
            self.page.views.append(GitView(self.page))

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

        # -------------------------------------------------------------------------------------------
        elif self.page.route == "/python_quiz_list":
            my_theme_color = '#e9c93a'
            topics = [{"topic_name": "Regular Expression", "topic_route": "/python_regex_quiz"}]
            self.page.views.append(TopicView(self.page, my_theme_color, topics))

        elif self.page.route == "/python_regex_quiz":
            file_path = "src/assets/regex_python_question_new.json"
            my_theme_color = '#e9c93a'
            self.page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN,)
            self.page.views.append(QuizView(self.page, file_path, my_theme_color))

        # -------------------------------------------------------------------------------------------
        elif self.page.route == "/mongodb_quiz_list":
            my_theme_color = '#ff99be'
            topics = [{"topic_name": "Mongo DB", "topic_route": "/mongodb_quiz"}]
            self.page.views.append(TopicView(self.page, my_theme_color, topics))

        elif self.page.route == "/mongodb_quiz":
            file_path = "src/assets/mongodb_question_new.json"
            my_theme_color = '#ff99be'
            self.page.theme = ft.Theme(color_scheme_seed="#FF99BE",)
            self.page.views.append(QuizView(self.page, file_path, my_theme_color))
        
        # -------------------------------------------------------------------------------------------
        elif self.page.route == "/linux_quiz_list":
            my_theme_color = '#eab676'
            topics = [{"topic_name": "Linux", "topic_route": "/linux_quiz"}]
            self.page.views.append(TopicView(self.page, my_theme_color, topics))

        elif self.page.route == "/linux_quiz":
            file_path = "src/assets/linux_question_new.json"
            my_theme_color = '#eab676'
            self.page.theme = ft.Theme(color_scheme_seed="#eab676",)
            self.page.views.append(QuizView(self.page, file_path, my_theme_color))

        self.page.update()

    def view_pop(self, view):
        """Handles back navigation."""
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


async def main(page: ft.Page):
    MyApp(page)  # Create an instance of MyApp

# ft.app(main, view=ft.AppView.WEB_BROWSER)
ft.app(main, assets_dir="assets")

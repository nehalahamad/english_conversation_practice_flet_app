import flet as ft


r = ft.Row()

class CustomProgressBar(ft.Row):
    def __init__(self, conversation, exercise, value=0):
        super().__init__()
        self.conversation = conversation
        self.exercise = exercise
        self.value = value
        self.spacing = 3
        self.controls = []

        self.add_conversation(conversation)
        self.add_exercise(exercise)
        self.update()

    def update(self):
        for i in range(int(self.value * (self.conversation + self.exercise))):
            self.controls[i].bgcolor = "green"
            self.update()


    def add_conversation(self, conversation):
        for i in range(conversation):
            self.controls.append(ft.Container(
                height=5,
                # bgcolor="blue",
                border=ft.border.all(color="blue", width=1),
                expand=True,
                border_radius=5,
                margin=0,
            ))
            self.update()
    def add_exercise(self, exercise):
        for i in range(exercise):
            self.controls.append(ft.Container(
                height=5,
                # bgcolor="green",
                border=ft.border.all(color="red", width=1),
                expand=True,
                border_radius=5,
                margin=0,
            ))
            self.update()
    


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    pb = CustomProgressBar(5, 8)
    page.add(pb)
    chapter = 0

    def next_chapter(e):
        chapter += 1
        pb.value = chapter/(5+8)
        pb.update()
        page.update()
    

    page.add(ft.ElevatedButton("Next", on_click=next_chapter))
    page.update()
    


ft.app(main)
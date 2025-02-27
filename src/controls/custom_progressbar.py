import flet as ft


class CustomContainer(ft.Container):
    def __init__(self, color="yellow"):
        super().__init__()
        self.height = 5
        self.border = ft.border.all(color=color, width=1)
        self.border_radius = 5
        self.expand = True
        self.margin = 0


class CustomProgressBar(ft.Row):
    def __init__(self, conversation, exercise, value=0):
        super().__init__()
        self.conversation = conversation
        self.exercise = exercise
        self.value = value
        self.spacing = 3
        self.controls = []

        self.add_conversation(self.conversation)
        self.add_exercise(self.exercise)

        self.current_pos = 0

        # for i in range(0, self.map_value(self.value, 0, self.conversation + self.exercise)):
        #     self.controls[i].bgcolor = "#3de5eb"

    def before_update(self):

        for i in range(0, self.conversation + self.exercise):
            self.controls[i].bgcolor = ft.Colors.GREY_200
        # self.add_conversation(self.conversation)
        # self.add_exercise(self.exercise)
        for i in range(0, self.map_value(self.value, 0, self.conversation + self.exercise)):
            self.controls[i].bgcolor = "#3de5eb"

        

    def add_conversation(self, conversation):
        for i in range(conversation):
            self.controls.append(CustomContainer(color="blue"))

    def add_exercise(self, exercise):
        for i in range(exercise):
            self.controls.append(CustomContainer(color="red"))

    def map_value(self, x, min_val=0, max_val=17):
        return min(int(x * (max_val - min_val + 1)), max_val) 
    


# def main(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


#     item = (0 + 12) / (5+8)
#     pb = CustomProgressBar(5, 8, item)
#     page.add(pb)

#     def next_chapter(e):
#         pb.value = item/(5+8)
#         pb.update()
#         page.update()
    

#     page.add(ft.ElevatedButton("Next", on_click=next_chapter))
#     page.update()
    


# ft.app(main)
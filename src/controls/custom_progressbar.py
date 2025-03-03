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
    def __init__(self, conversation_len, exercise_len, value=0):
        super().__init__()
        self.conversation_len = conversation_len
        self.exercise_len = exercise_len
        self.value = value
        self.spacing = 3
        self.controls = []
        self.before_update()


    def before_update(self):
        self.controls = []
        # adding conversation bar
        self.add_conversation(self.conversation_len)
        # adding exercise bar
        self.add_exercise(self.exercise_len)
        # making background of the bar to grey
        for i in range(0, self.conversation_len + self.exercise_len):
            self.controls[i].bgcolor = ft.Colors.GREY_200
        
        for i in range(0, self.map_value(self.value, 0, self.conversation_len + self.exercise_len)):
            self.controls[i].bgcolor = "#3de5eb"


    def add_conversation(self, conversation_len):
        for i in range(conversation_len):
            self.controls.append(CustomContainer(color="blue"))


    def add_exercise(self, exercise_len):
        for i in range(exercise_len):
            self.controls.append(CustomContainer(color="red"))


    def map_value(self, x, min_val=0, max_val=17):
        return min(int(x * (max_val - min_val + 1)), max_val) 

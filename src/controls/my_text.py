import flet as ft

class MyText(ft.Text):
    def __init__(self, value, size=18, color=ft.Colors.BLACK, selectable=True):
        super().__init__()
        self.value = value
        self.size = size
        self.selectable = selectable
        self.color = color
        self.no_wrap = False
import flet as ft


question = {
    "QN": "1",
    "type": "mcq",
    "question": "To increase the response time and throughput, the kernel minimizes the frequency of disk access by keeping a pool of internal data buffer called",
    "options": {
        "A": "Pooling",
        "B": "Spooling",
        "C": "Buffer cache",
        "D": "Swapping"
    },
    "answer": "C",
    "explanation": "None."
}


class MyContainer(ft.Container):
    def __init__(self, page, key, value, ref, on_click):
        super().__init__()
        self.margin = 0
        self.content = ft.Stack(
            controls=[
                ft.Container(
                    content=ft.Text(value=value, text_align=ft.TextAlign.LEFT, no_wrap=False, width=page.width, size=15, selectable=False),
                    padding=10,
                    margin=ft.margin.only(left=5, right=5, top=12, bottom=0),
                    border_radius=5,
                    border=ft.border.all(1, ft.Colors.GREY),
                    bgcolor=ft.Colors.WHITE,
                    ref=ref,
                    on_click=on_click

                ),
                ft.Container(
                    content=ft.Text(value=key, size=12, weight=ft.FontWeight.BOLD),
                    margin=ft.margin.only(left=15),
                    padding=ft.padding.only(left=5, right=5, bottom=3),
                    border_radius=5,
                    border=ft.border.all(1, ft.Colors.GREY),
                    bgcolor=ft.Colors.WHITE,
                )
            ],
        )

def main(page: ft.Page):
    page.title = 'Container group'
    page.window.width = 360
    def button_clicked(e):
        print(e.control.content.value)
        for ref in ref_list:
            ref.current.border = ft.border.all(1, ft.Colors.GREY)
        e.control.border = ft.border.all(1, ft.Colors.BLUE)
        page.update()

    ref_list = []
    column = ft.Column()
    for key, value in question['options'].items():
        ref = ft.Ref[ft.Container]()
        ref_list.append(ref)
        column.controls.append(
            MyContainer(page, key, value, ref, on_click = button_clicked)
        )
    page.add(column)


ft.app(main)
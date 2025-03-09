import flet as ft


def main(page):
    

    page.add(
        ft.Stack(
            controls=[
                # ft.Text('nehal ahamad ansari nehal ahamad ansari', left=30, no_wrap=False, width=200),
                ft.Container(
                    content=ft.Radio(width=400),
                    border=ft.border.all(1, ft.Colors.AMBER_800),
                    width=200,
                    alignment=ft.alignment.center_left,
                    # left=20
                )
            ],
            width=200
        )
    )


ft.app(main)
import flet as ft

def main(page: ft.Page):
    st = ft.Stack(
        [
            ft.Container(
                content=ft.Text('Question: 5 adfas  dfa asdfas asfas safa asdfa assfas adfas  dfa asdfas asfas safa asdfa assfas adfas  dfa asdfas asfas safa asdfa assfas '),
                padding=10,
                margin=ft.margin.only(left=5, right=5, top=15, bottom=5),
                border_radius=5,
                border=ft.border.all(1, 'red'),
                bgcolor=ft.Colors.WHITE,
            ),
            ft.Container(
                content=ft.Text('Question: 5'),
                margin=ft.margin.only(left=15),
                border_radius=5,
                border=ft.border.all(1, 'red'),
                bgcolor=ft.Colors.WHITE,

            )

        ],
    )

    page.add(st)

ft.app(main)
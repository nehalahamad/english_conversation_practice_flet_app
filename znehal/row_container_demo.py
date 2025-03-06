import flet as ft


def main(page: ft.Page):
    page.bgcolor='green'
    page.window.width = 500
    cc = ft.Row(
        controls=[
            ft.Container(
                content=ft.Radio(
                    label=ft.Text("Another long label for testing text wrapping in radio buttons", width=200),
                    width=200
                ),
                # width=100,
                bgcolor='red'
            ),
            # ft.Container(
            #     content=ft.Text('nehal adfadsaf  adsfsa afdsa  asf fds aas  afaas  afasf    fdf', no_wrap=False),
            #     width=page.width-20
            # ),
        ],
        # width=30,
    ) 

    page.add(cc)



ft.app(main)
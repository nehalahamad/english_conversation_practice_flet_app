import flet as ft


def main(page: ft.Page):
    cc = ft.Row(
        controls=[
            ft.Radio(),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text('nehal adfas  afas  adfa  afdas  afasf    fadasf   asfaf  a faf   fdf', no_wrap=False),
                        width=300,
                        bgcolor='green'
                    ),
                ],
                scroll=True,

            ),
        ],
    )

    page.add(cc)



ft.app(main)
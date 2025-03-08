import flet as ft



def main(page: ft.Page):
    page.window.width=360
    page.window.height=640
    # page.scroll=True
    page.add(
        ft.Column(
            controls=[
                ft.Container(height=50, bgcolor='red'),
                ft.Container(height=50, bgcolor='red'),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                            ft.Text('adsfsdf asfasd fsdsd fasd'),
                        ],
                        scroll=True
                    ),
                    bgcolor='red'
                    ),
                ft.Container(
                    height=200, 
                    bgcolor='green', expand=True),
                ft.Container(height=50, bgcolor='red'), 
            ],
            expand=True,
            # scroll=True,
            # height=page.height,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN

        )
    )


ft.app(main)
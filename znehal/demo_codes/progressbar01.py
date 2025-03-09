from time import sleep

import flet as ft

def main(page: ft.Page):
    pb = ft.ProgressBar(
        semantics_label='kkkkk',
        height=20,
        bar_height= 30,
        col = 10
    )

    page.add(
        ft.Text("Linear progress indicator", style="headlineSmall"),
        ft.Column([ ft.Text("Doing something..."), pb]),
        # ft.Text("Indeterminate progress bar", style="headlineSmall"),
        # ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee"),
    )

    for i in range(0, 101):
        pb.value = i * 0.01
        sleep(1)
        page.update()

ft.app(main)
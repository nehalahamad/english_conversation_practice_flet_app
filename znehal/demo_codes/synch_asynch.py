import flet as ft
import time, asyncio
import os

# os.environ["FLET_FORCE_WEB_SERVER"] = 'true'


def main(page: ft.Page):
    def handler(e):
        '''this handler is running using threading.Thread'''
        time.sleep(3)
        page.add(ft.Text("Handler clicked"))

    async def handler_async(e):
        '''this handler is running using asyncio.Task'''
        await asyncio.sleep(3)
        page.add(ft.Text("Async handler clicked"))

    page.add(
        ft.ElevatedButton("Call handler", on_click=handler),
        ft.ElevatedButton("Call async handler", on_click=handler_async) 
    )



ft.app(target=main)
import flet as ft

def main(page: ft.Page):
    page.title = "Radio Button with Wrapped Label"
    page.padding = 20
    page.scroll = "adaptive"  # Enable scrolling if needed

    def on_change(e):
        selected_value.value = f"Selected: {radio_group.value}"
        page.update()

    radio_group = ft.RadioGroup(
        content=ft.Column([
            ft.Container(
                content=ft.Radio(value="option1", label="This is a long label text that should wrap properly This is a long label text that should wrap properly his is a long label text that should wrap properly This is a long label text that should wrap properly This is a long label text that should wrap properly"),
                width=10,  # Set width relative to the page
                bgcolor='pink'
            ),
            ft.Container(
                content=ft.Radio(value="option2", label="Another long label for testing text wrapping in radio buttons"),
                width=page.width * 0.9,  # Set width relative to the page
            ),
        ], wrap=True),  # Ensures wrapping when needed 
        on_change=on_change
    )

    selected_value = ft.Text("Selected: None")

    page.add(radio_group, selected_value)

ft.app(target=main)

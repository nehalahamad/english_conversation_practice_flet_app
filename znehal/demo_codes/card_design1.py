import flet as ft

def main(page: ft.Page):
    page.title = "Card Designs"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Design 1: Simple Card
    card1 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("John Doe", size=20, weight="bold"),
                    ft.Text("123 Main St, Springfield, IL, 62701"),
                ],
                spacing=5,
            ),
            padding=20,
        ),
        elevation=5,
        margin=10,
    )

    # Design 2: Card with a colored background
    card2 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Jane Smith", size=20, weight="bold", color="white"),
                    ft.Text("456 Elm St, Shelbyville, IL, 62702 456 Elm St, Shelbyville, IL, 62702", color="white"),
                ],
                spacing=5,
            ),
            padding=20,
            bgcolor=ft.colors.BLUE_500,
        ),
        elevation=5,
        margin=10,
    )

    # Design 3: Card with an icon
    card3 = ft.Card(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Icon(ft.icons.LOCATION_ON, color=ft.colors.RED, size=40),
                    ft.Column(
                        [
                            ft.Text("Alice Johnson", size=20, weight="bold"),
                            ft.Text("789 Oak St, Capital City, IL, 62703"),
                        ],
                        spacing=5,
                    ),
                ],
                spacing=10,
            ),
            padding=20,
        ),
        elevation=5,
        margin=10,
    )

    # Design 4: Card with a border
    card4 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Bob Brown", size=20, weight="bold"),
                    ft.Text("321 Pine St, Metropolis, IL, 62704"),
                ],
                spacing=5,
            ),
            padding=20,
            border=ft.border.all(2, ft.colors.GREY_500),
        ),
        elevation=5,
        margin=10,
    )

    # Add all cards to the page
    page.add(card1, card2, card3, card4)

ft.app(target=main)
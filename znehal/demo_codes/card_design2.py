import flet as ft

def main(page: ft.Page):
    page.title = "Card Designs with Scrolling and Animation"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.scroll = True

    # Design 1: Simple Card with Scrollable Address
    card1 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("John Doe", size=20, weight="bold"),
                    ft.Column(
                        [
                            ft.Text(
                                "123 Main St, Springfield, IL, 62701\n"
                                "Additional Address Line 1\n"
                                "Additional Address Line 2\n"
                                "Additional Address Line 3\n"
                                "Additional Address Line 4",
                                size=14,
                            ),
                        ],
                        scroll=True,
                        height=100,  # Set a fixed height for the scrollable area
                    ),
                ],
                spacing=5,
            ),
            padding=20,
        ),
        elevation=5,
        margin=10,
    )

    # Design 2: Card with a colored background and hover animation
    card2 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Jane Smith", size=20, weight="bold", color="white"),
                    ft.Column(
                        [
                            ft.Text(
                                "456 Elm St, Shelbyville, IL, 62702\n"
                                "Additional Address Line 1\n"
                                "Additional Address Line 2",
                                size=14,
                                color="white",
                            ),
                        ],
                        scroll=True,
                        height=100,
                    ),
                ],
                spacing=5,
            ),
            padding=20,
            bgcolor=ft.colors.BLUE_500,
            on_hover=lambda e: animate_card(e, card2),
        ),
        elevation=5,
        margin=10,
    )

    # Design 3: Card with an icon and rotation animation
    card3 = ft.Card(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Icon(ft.icons.LOCATION_ON, color=ft.colors.RED, size=40),
                    ft.Column(
                        [
                            ft.Text("Alice Johnson", size=20, weight="bold"),
                            ft.Column(
                                [
                                    ft.Text(
                                        "789 Oak St, Capital City, IL, 62703\n"
                                        "Additional Address Line 1\n"
                                        "Additional Address Line 2",
                                        size=14,
                                    ),
                                ],
                                scroll=True,
                                height=100,
                            ),
                        ],
                        spacing=5,
                    ),
                ],
                spacing=10,
            ),
            padding=20,
            on_hover=lambda e: rotate_icon(e, card3),
        ),
        elevation=5,
        margin=10,
    )

    # Design 4: Card with a border and scaling animation
    card4 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Bob Brown", size=20, weight="bold"),
                    ft.Column(
                        [
                            ft.Text(
                                "321 Pine St, Metropolis, IL, 62704\n"
                                "Additional Address Line 1\n"
                                "Additional Address Line 2",
                                size=14,
                            ),
                        ],
                        scroll=True,
                        height=100,
                    ),
                ],
                spacing=5,
            ),
            padding=20,
            border=ft.border.all(2, ft.colors.GREY_500),
            on_hover=lambda e: scale_card(e, card4),
        ),
        elevation=5,
        margin=10,
    )

    # Design 5: Card with gradient background and fade animation
    card5 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Eva Green", size=20, weight="bold", color="white"),
                    ft.Column(
                        [
                            ft.Text(
                                "654 Birch St, Smalltown, IL, 62705\n"
                                "Additional Address Line 1\n"
                                "Additional Address Line 2",
                                size=14,
                                color="white",
                            ),
                        ],
                        scroll=True,
                        height=100,
                    ),
                ],
                spacing=5,
            ),
            padding=20,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[ft.colors.PURPLE, ft.colors.PINK],
            ),
            on_hover=lambda e: fade_card(e, card5),
        ),
        elevation=5,
        margin=10,
    )

    # Add all cards to the page
    page.add(card1, card2, card3, card4, card5)

    # Animation functions
    def animate_card(e, card):
        if e.data == "true":
            card.content.bgcolor = ft.colors.BLUE_700
            card.elevation = 10
        else:
            card.content.bgcolor = ft.colors.BLUE_500
            card.elevation = 5
        card.update()

    def rotate_icon(e, card):
        icon = card.content.content.controls[0]
        if e.data == "true":
            icon.rotate = ft.transform.Rotate(0.5, alignment=ft.alignment.center)
        else:
            icon.rotate = ft.transform.Rotate(0, alignment=ft.alignment.center)
        card.update()

    def scale_card(e, card):
        if e.data == "true":
            card.content.scale = ft.transform.Scale(1.05, alignment=ft.alignment.center)
        else:
            card.content.scale = ft.transform.Scale(1, alignment=ft.alignment.center)
        card.update()

    def fade_card(e, card):
        if e.data == "true":
            card.content.opacity = 0.8
        else:
            card.content.opacity = 1
        card.update()

ft.app(target=main)
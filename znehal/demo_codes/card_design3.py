import flet as ft
import random
import time

# --- Card Data ---
card_data = [
    {"title": "Sunrise Serenity", "subtitle": "A calming sunrise scene", "image": "https://images.unsplash.com/photo-1506905925348-9c6bd1a9dfac?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8c2VhfGVufDB8fDB8fHww&auto=format&fit=crop&w=600&q=60"},
    {"title": "Mountain Majesty", "subtitle": "A breathtaking mountain view", "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fG1vdW50YWlufGVufDB8fDB8fHww&auto=format&fit=crop&w=600&q=60"},
    {"title": "Forest Whisper", "subtitle": "The peaceful sounds of nature", "image": "https://images.unsplash.com/photo-1574680098655-12d8f0a0724a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Zm9yZXN0fGVufDB8fDB8fHww&auto=format&fit=crop&w=600&q=60"},
    {"title": "Starry Night Dream", "subtitle": "Lost in the vastness of space", "image": "https://images.unsplash.com/photo-1554034483-04fda0d3507b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHN0YXJyeSUyMG5pZ2h0fGVufDB8fDB8fHww&auto=format&fit=crop&w=600&q=60"},
]


class AnimatedCard(ft.Container):
    def __init__(self, card_data, on_hover_color=ft.Colors.BLUE_GREY_100):
        super().__init__()
        self.card_data = card_data
        self.width = 300
        self.height = 200
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = ft.border_radius.all(10)
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=5,
            color=ft.Colors.BLACK,
            offset=ft.Offset(0, 2),
        )
        self.scale = 1
        self.rotate = 0
        self.animate_scale = ft.animation.Animation(500, ft.AnimationCurve.EASE)
        self.animate_rotation = ft.animation.Animation(500, ft.AnimationCurve.EASE)
        self.on_hover_color = on_hover_color
        self.content = self.build_content()
        self.ink = True
        self.on_hover = self.hover

    def build_content(self):
        return ft.Column(
            [
                ft.Image(
                    src=self.card_data["image"],
                    fit=ft.ImageFit.COVER,
                    height=120,
                ),
                ft.ListTile(
                    title=ft.Text(self.card_data["title"]),
                    subtitle=ft.Text(self.card_data["subtitle"]),
                ),
            ],
        )

    def hover(self, e):
        self.scale = 1.1 if self.scale == 1 else 1
        self.rotate = 0.02 if self.rotate == 0 else 0
        self.update()


def main(page: ft.Page):
    page.title = "Animated Cards"
    page.padding = 50
    page.bgcolor = ft.Colors.BLUE_GREY_50

    # Create a list of AnimatedCard widgets
    cards = [
        ft.Container(
            content=AnimatedCard(data),
            col={"sm": 6, "md": 4},
        )
        for data in card_data
    ]

    page.add(
        ft.Row(
            controls=cards,
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
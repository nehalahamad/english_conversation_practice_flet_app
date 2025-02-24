from enum import Enum
import flet as ft
from typing import Union, Optional, List, Dict
import random

class MyColors(str, Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

print(ft.Colors.RED)
print(MyColors.RED)

class Colors(str, Enum):
    @staticmethod
    def with_opacity(opacity: Union[int, float], color: "ColorValue") -> str:
        assert 0 <= opacity <= 1, "opacity must be between 0 and 1"
        color_str = color.value if isinstance(color, Enum) else color
        return f"{color_str},{opacity}"

    @staticmethod
    def random(
        exclude: Optional[List["Colors"]] = None,
        weights: Optional[Dict["Colors", int]] = None,
    ) -> Optional["Colors"]:
        """
        Selects a random color, with optional exclusions and weights.

        Args:
            exclude: A list of colors members to exclude from the selection.
            weights: A dictionary mapping color members to their respective weights for weighted random selection.

        Returns:
            A randomly selected color, or None if all members are excluded.
        """
        choices = list(Colors)
        if exclude:
            choices = [member for member in choices if member not in exclude]
            if not choices:
                return None
        if weights:
            weights_list = [weights.get(c, 1) for c in choices]
            return random.choices(choices, weights=weights_list)[0]
        return random.choice(choices)

    PRIMARY = "primary"
    ON_PRIMARY = "onprimary"
    PRIMARY_CONTAINER = "primarycontainer"
    ON_PRIMARY_CONTAINER = "onprimarycontainer"
    SECONDARY = "secondary"
    ON_SECONDARY = "onsecondary"
    SECONDARY_CONTAINER = "secondarycontainer"
    ON_SECONDARY_CONTAINER = "onsecondarycontainer"
    RED = "red"


def main(page: ft.Page):
    page.add(ft.Container(width=100, height=100, bgcolor=ft.Colors.ON_SECONDARY_CONTAINER))
    
ft.app(main)
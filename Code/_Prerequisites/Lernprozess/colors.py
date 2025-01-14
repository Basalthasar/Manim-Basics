from manim import *

class ShowColors(Scene):
    def construct(self):
        colors = [
            RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, TEAL, GOLD, MAROON, PINK,
            LIGHT_BROWN, DARK_BROWN, GREY, LIGHT_GREY, DARK_GREY, WHITE, BLACK
        ]
        color_names = [
            "RED", "GREEN", "BLUE", "YELLOW", "PURPLE", "ORANGE", "TEAL", "GOLD", "MAROON", "PINK",
            "LIGHT_BROWN", "DARK_BROWN", "GREY", "LIGHT_GREY", "DARK_GREY", "WHITE", "BLACK"
        ]

        squares_and_labels = VGroup()

        for i, color in enumerate(colors):
            square = Square(side_length=1, fill_color=color, fill_opacity=1)
            label = Text(color_names[i], font_size=24)
            square.next_to(label, UP)
            squares_and_labels.add(VGroup(square, label))

        grid = squares_and_labels.arrange_in_grid(rows=3, cols=6, buff=0.5)
        self.play(Create(grid))
        self.wait(2)

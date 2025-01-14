# Import
from manim import * 

"""
Bottom left corner (-4 | -7.1)

Top right edge (4 | 7.1)
"""


# Eine dedizierte Klasse eignet sich für eine Szene
class HelloWorld(Scene):
    def construct(self):
        
        # Objekt kreirt
        sq = Square(
            side_length=5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75
        )

        # Objekt abgebildet, für 5 Sekunden
        self.play(Create(sq), run_time=5)
        
        # 1 Sekunde gewartet
        self.wait()

class Testing(Scene):
    def construct(self):

        # Etwas Text, welcher zur Ecke DR (=> Down Right) mit "buff"-Effekt (TODO: What does it do) verschoben wird
        text = Tex("$(Hello World)^2$").to_edge(DR, buff=0.5)

        # Ein Quadrat mit Seitenlänge 0.5, mit Füllfarbe Grün, welches um 3 Einheiten nach links verschoben wird.
        # stroke_color kontrolliert die Füllfarbe und nicht fill_color, warum auch immer ?? 
        sq = Square(

            side_length=0.5, stroke_color=GREEN, fill_color=PURPLE, fill_opacity=0.75
            
            ).shift(LEFT*3)

        # Ein Dreieck, welches um 0.6 verkleinert wird, und daraufhin an die UL (Upper Left) Ecke verschoben wird
        tri = Triangle().scale(0.6).to_edge(UL)

        self.play(Write(text))
        self.play(DrawBorderThenFill(sq), run_time=2)
        self.play(Create(tri))
        self.wait(5)

class selfproduced(Scene):
    def construct(self):

        # Farben in mAnim
        default_colors = [
            RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK, MAROON, GOLD, LIGHT_GRAY, GRAY, DARK_BROWN, BLACK, WHITE
        ]

        # Alle Objekte erzeugen
        squares = []
        for i in range(len(default_colors)):
            square = Square(side_length=1, stroke_color=default_colors[i])
            squares.append(square)

        # Anordnen
        squares_group = VGroup(*squares).arrange(RIGHT, buff=0.0001)
        
        # Spielen
        self.play(Create(squares_group))

        # Warten
        self.wait(5)
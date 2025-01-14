from manim import *

class Ableitung(Scene):

    def construct(self):
        # Graph groß
        Achsen = Axes(
            x_range=[-0.5, 2.5],
            y_range=[-0.5, 3],
            axis_config={"color": WHITE}
        )
        Achsenbeschriftung = Achsen.get_axis_labels(x_label="x", y_label="y")
        
        # Nummerierung hinzufügen
        Achsen.add_coordinates()

        Graph = Achsen.plot(lambda x: 0.5*x**2, color=GOLD)
        
        Funktionsterm = MathTex(r"f(x) = \frac{1}{2}x^2", color=GOLD)
        Funktionsterm.next_to(Graph, RIGHT)
        Funktionsterm.shift(DOWN * 1.25, LEFT * 3.5)

        Graph_ganz = VGroup(Achsen, Achsenbeschriftung, Graph, Funktionsterm)

        # Einfaden der Achsen, Achsenbeschriftung und des Graphen
        self.play(Create(Achsen))
        self.wait(0.25)
        self.play(Write(Achsenbeschriftung))
        self.wait(0.25)
        self.play(Create(Graph))
        self.wait(0.25)
        self.play(Write(Funktionsterm))
        self.wait(10)


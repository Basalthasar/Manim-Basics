from manim import *

class Extremata(Scene):
    def construct(self):
        # Titel
        titel = Text("Extremstellen", font="Georgia", font_size=96) 
        titel.move_to(ORIGIN)
        self.play(titel.animate.scale(0.65).shift(UP*3.1), run_time=2)
        self.wait(1)

        # Funktion, Achsen und Graph
        # TOFIX: Schrittweite der Achsenbeschriftung verkleinern
        achsen = Axes(
            x_range=[-1.5, 1],
            y_range=[-0.5, 0.5],
            axis_config={"color": WHITE},
            x_axis_config={"tick_size": 0.1, "unit_size": 0.5},
            y_axis_config={"tick_size": 0.1, "unit_size": 0.5},
        )
        achsenbeschriftung = achsen.get_axis_labels(x_label="x", y_label="y", )
        achsen.add_coordinates()

        funktion = achsen.plot(lambda x: x**3 + x**2, x_range=[-1.25, 0.625], color=GOLD)

        funktionsterm = MathTex("f(x) = x^3 + x^2", color=GOLD)
        funktionsterm.next_to(funktion, buff=0.01)
        funktionsterm.shift(UP)

        graph_ganz = VGroup(achsen, achsenbeschriftung, funktion, funktionsterm)
        graph_ganz.scale(0.95).shift(DOWN*0.75)

        # Achsen und Graph
        self.play(Create(achsen))
        self.wait(0.25)
        self.play(Write(achsenbeschriftung))
        self.wait(0.25)
        self.play(Create(funktion))
        self.wait(0.25)
        self.play(Write(funktionsterm))
        self.play(graph_ganz.animate.shift(LEFT * 2).scale(0.8), run_time=2)
        self.wait(2)

        # Extremstellen
        # TOFIX: Punkte an den Extremata stoppen, fixen
        hochpunkt = Dot(achsen.c2p(-2/3, 4/27), color=RED)
        tiefpunkt = Dot(achsen.c2p(0, 0), color=BLUE)
        self.play(
            AnimationGroup(
                MoveAlongPath(hochpunkt, funktion, rate_func=linear, run_time=2),
                MoveAlongPath(tiefpunkt, funktion, rate_func=linear, run_time=2),
                lag_ratio=0
            )
        )

        self.wait(2)
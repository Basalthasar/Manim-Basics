from manim import *

class Ableitung(Scene):

    def construct(self):
        # Titel
        Titel = Text("Was ist eine Ableitung?", font="Georgia", font_size=96) 
        Titel.move_to(ORIGIN)
        self.play(Titel.animate.scale(0.65).shift(UP*3), run_time=2)
        self.wait(1)

        # Achsen und Graph
        Achsen = Axes(
            x_range=[-0.5, 2.5],
            y_range=[-0.5, 3],
            axis_config={"color": WHITE}
        )
        Achsenbeschriftung = Achsen.get_axis_labels(x_label="x", y_label="y")
        Achsen.add_coordinates()

        Graph = Achsen.plot(lambda x: 0.5*x**2, color=GOLD)
        
        Funktionsterm = MathTex(r"f(x) = \frac{1}{2}x^2", color=GOLD)
        Funktionsterm.next_to(Graph, RIGHT)
        Funktionsterm.shift(DOWN * 1.25, LEFT * 3.5)

        Graph_ganz = VGroup(Achsen, Achsenbeschriftung, Graph, Funktionsterm)
        Graph_ganz.scale(0.95).shift(DOWN*0.75)

        # Einfaden der Achsen, Achsenbeschriftung und des Graphen
        self.play(Create(Achsen))
        self.wait(0.25)
        self.play(Write(Achsenbeschriftung))
        self.wait(0.25)
        self.play(Create(Graph))
        self.wait(0.25)
        self.play(Write(Funktionsterm))
        self.play(Graph_ganz.animate.shift(LEFT * 2).scale(0.8), run_time=2)
        self.wait(2)

        # 1. Durchschnittliche Steigung beschreiben
        Stichpunkt1 = MathTex(
            r"\text{Zwei Punkte auf}",
            r"\\", # Für einen Zeilenumbruch
            r"\text{der Funktion:}",
            r"\\",
            r"p_1", r"\text{ und }", r"p_2"
        )
        Stichpunkt1[4].set_color(PURE_RED)
        Stichpunkt1[6].set_color(PURE_RED)
        Stichpunkt1.next_to(Graph_ganz, RIGHT*2)

        self.play(Write(Stichpunkt1), run_time=1)

        # Punkte auf dem Graphen
        p1 = Dot(Achsen.c2p(0, 0), color=PURE_RED)
        p2 = Dot(Achsen.c2p(0, 0), color=PURE_RED)
        p1_label = MathTex("p_1", color=PURE_RED).next_to(p1, DOWN)

        self.play(FadeIn(p1, p1_label))
        self.play(FadeIn(p2))

        # Pfad für p2 entlang des Graphen
        origin = Achsen.c2p(0, 0)
        graph_end = Graph.point_from_proportion((1.5 - Graph.t_min) / (Graph.t_max - Graph.t_min))

        # Pfad entlang des Graphen von 0 bis 1.5
        path_along_graph = Graph.get_subcurve((0 - Graph.t_min) / (Graph.t_max - Graph.t_min), (1.5 - Graph.t_min) / (Graph.t_max - Graph.t_min))

        # Kombinierter Pfad
        combined_path = VMobject()
        combined_path.set_points_as_corners([origin])
        combined_path.append_points(path_along_graph.get_points())

        self.play(MoveAlongPath(p2, combined_path), run_time=2)

        p2_label = MathTex("p_2", color=PURE_RED).next_to(p2, UP)
        self.play(FadeIn(p2_label))

        # Vertikale Linie von p2 zur x-Achse
        vert_line = DashedLine(start=p2.get_bottom(), end=Achsen.c2p(1.5, 0), color=WHITE)
        self.play(Create(vert_line))

        # Gerade durch p1 und p2, verlängert
        secant_line = Line(
            start=p1.get_center(), 
            end=p2.get_center(), 
            color=RED
        )
        secant_line.scale(1.25, about_point=secant_line.get_start())
        secant_line.scale(1.25, about_point=secant_line.get_end())
        secant_line.set_z_index(-3)  # Setzt den z-index auf einen niedrigeren Wert, um die Sekante hinter den Graphen zu legen

        self.play(Create(secant_line))

        self.play(Stichpunkt1.animate.scale(0.75).shift(UP*1.5), run_time=1)

        self.wait(2)

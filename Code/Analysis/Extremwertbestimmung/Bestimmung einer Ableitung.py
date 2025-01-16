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

        # Achsen und Graph
        self.play(Create(Achsen))
        self.wait(0.25)
        self.play(Write(Achsenbeschriftung))
        self.wait(0.25)
        self.play(Create(Graph))
        self.wait(0.25)
        self.play(Write(Funktionsterm))
        self.play(Graph_ganz.animate.shift(LEFT * 2).scale(0.8), run_time=2)
        self.wait(2)

        # Punkte auf dem Graphen
        Stichpunkt1 = MathTex(
            r"\text{Zwei Punkte auf}",
            r"\\",
            r"\text{der Funktion:}",
            r"\\",
            r"p_1", r"\text{ und }", r"p_2"
        )
        Stichpunkt1[4].set_color(PURE_RED)
        Stichpunkt1[6].set_color(PURE_RED)
        Stichpunkt1.next_to(Graph_ganz, RIGHT*2)

        self.play(Write(Stichpunkt1), run_time=1)

        p1 = Dot(Achsen.c2p(0, 0), color=PURE_RED)
        p2 = Dot(Achsen.c2p(0, 0), color=PURE_RED)
        p1_label = MathTex("p_1", color=PURE_RED).next_to(p1, DOWN)

        self.play(FadeIn(p1, p1_label))
        self.play(FadeIn(p2))

        # p2 entlang des Graphen bewegen
        origin = Achsen.c2p(0, 0)
        graph_end = Graph.point_from_proportion((1.5 - Graph.t_min) / (Graph.t_max - Graph.t_min))

        path_along_graph = Graph.get_subcurve((0 - Graph.t_min) / (Graph.t_max - Graph.t_min), (1.5 - Graph.t_min) / (Graph.t_max - Graph.t_min))

        combined_path = VMobject()
        combined_path.set_points_as_corners([origin])
        combined_path.append_points(path_along_graph.get_points())

        self.play(MoveAlongPath(p2, combined_path), run_time=2)

        p2_label = MathTex("p_2", color=PURE_RED).next_to(p2, UP)
        self.play(FadeIn(p2_label))

        # Vertikale Linie von p2 zur x-Achse
        vert_line = DashedLine(start=p2.get_bottom(), end=Achsen.c2p(1.5, 0), color=WHITE)
        self.play(Create(vert_line))

        # Sekantenlinie zwischen p1 und p2
        secant_line = Line(
            start=p1.get_center(), 
            end=p2.get_center(), 
            color=RED
        )
        midpoint = (p1.get_center() + p2.get_center()) / 2
        direction = p2.get_center() - p1.get_center()
        direction /= np.linalg.norm(direction)
        fixed_length = 8
        secant_line.put_start_and_end_on(midpoint - direction * (fixed_length / 2), midpoint + direction * (fixed_length / 2))
        secant_line.set_z_index(-3)

        self.play(Create(secant_line))

        self.play(Stichpunkt1.animate.scale(0.75).shift(UP*1.75), run_time=1)

        self.wait(2)

        # Zweiter Punkt nähert sich dem ersten Punkt
        Stichpunkt2 = MathTex(
            r"p_1", r"\text{ und }", r"p_2", r"\text{ sich}",
            r"\\",
            r"\text{annähern lassen}"
        )
        Stichpunkt2[0].set_color(PURE_RED)
        Stichpunkt2[2].set_color(PURE_RED)
        
        Stichpunkt2.next_to(Stichpunkt1, DOWN)
        Stichpunkt2.scale(0.75)

        self.play(Write(Stichpunkt2), run_time=1)
        path_along_graph_p1 = Graph.get_subcurve((0 - Graph.t_min) / (Graph.t_max - Graph.t_min), (1.499999 - Graph.t_min) / (Graph.t_max - Graph.t_min))

        combined_path_p1 = VMobject()
        combined_path_p1.set_points_as_corners([origin])
        combined_path_p1.append_points(path_along_graph_p1.get_points())

        p1_label_path = combined_path_p1.copy()
        p1_label_path.shift(DOWN * 0.5)

        # Sekantenlinie aktualisieren, während sich p1 bewegt
        def update_secant_line(line):
            start = p1.get_center()
            end = p2.get_center()
            midpoint = (start + end) / 2
            direction = end - start
            direction /= np.linalg.norm(direction)
            fixed_length = 8
            line.put_start_and_end_on(midpoint - direction * (fixed_length / 2), midpoint + direction * (fixed_length / 2))

        secant_line.add_updater(update_secant_line)

        # Tangente bei p2
        tangent_line = TangentLine(Graph, alpha=(1.5 - Graph.t_min) / (Graph.t_max - Graph.t_min), length=8, color=RED)

        self.play(FadeOut(vert_line))
        self.play(
            MoveAlongPath(p1, combined_path_p1), 
            MoveAlongPath(p1_label, p1_label_path),
            run_time=2
        )

        secant_line.remove_updater(update_secant_line)
        
        self.play(Transform(secant_line, tangent_line), run_time=2)

        self.wait(1)

        self.play(Funktionsterm.animate.shift(UP*1.5 + LEFT*3), run_time=0.5)

        # Steigungsdreieck an der Tangente
        x0 = 1.5
        h = 0.5
        x1 = x0 + h
        y0 = 0.5 * x0**2
        y1 = 0.5 * x0**2 + (x1 - x0) * x0 + 0.03

        # Punkte des Steigungsdreiecks
        p3 = Dot(Achsen.c2p(x1, y0), color=BLUE)
        p4 = Dot(Achsen.c2p(x1, y1), color=BLUE)

        # Linien des Steigungsdreiecks
        horizontal_line = DashedLine(start=p2.get_center(), end=p3.get_center(), color=WHITE)
        vertical_line = DashedLine(start=p3.get_center(), end=p4.get_center(), color=WHITE)
        horizontal_line.set_z_index(-1)
        vertical_line.set_z_index(-1)

        self.play(FadeIn(p3), FadeIn(p4))
        self.play(Create(horizontal_line), Create(vertical_line))

        # Steigungsdreieck beschriften
        delta_x = MathTex(r"\Delta x", color=BLUE).next_to(horizontal_line, DOWN)
        delta_y = MathTex(r"\Delta y", color=BLUE).next_to(vertical_line, RIGHT)

        self.play(Write(delta_x), Write(delta_y))

        # Steigungsdreieck Formel
        slope_formula = MathTex(
            r"\text{Steigung} = \frac{\Delta y}{\Delta x}",
            r"\\",
            r"= \frac{f(x_0 + h) - f(x_0)}{h}",
            color=BLUE
        ) # TOFIX: Limes hinzufügen
        slope_formula.next_to(Stichpunkt2, DOWN)
        slope_formula.scale(0.75)

        self.play(Write(slope_formula))

        self.wait(2)
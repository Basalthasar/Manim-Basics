from manim import *

class Ableitung(Scene):

    def construct(self):
        # Titel
        titel = Text("Was ist eine Ableitung?", font="Georgia", font_size=96) 
        titel.move_to(ORIGIN)
        self.play(titel.animate.scale(0.65).shift(UP*3), run_time=2)
        self.wait(1)

        # Achsen und Graph
        achsen = Axes(
            x_range=[-0.5, 2.5],
            y_range=[-0.5, 3],
            axis_config={"color": WHITE}
        )
        achsenbeschriftung = achsen.get_axis_labels(x_label="x", y_label="y")
        achsen.add_coordinates()

        graph = achsen.plot(lambda x: 0.5*x**2, color=GOLD)
        
        funktionsterm = MathTex(r"f(x) = \frac{1}{2}x^2", color=GOLD)
        funktionsterm.next_to(graph, RIGHT)
        funktionsterm.shift(DOWN * 1.25, LEFT * 3.5)

        graph_ganz = VGroup(achsen, achsenbeschriftung, graph, funktionsterm)
        graph_ganz.scale(0.95).shift(DOWN*0.75)

        # Achsen und Graph
        self.play(Create(achsen))
        self.wait(0.25)
        self.play(Write(achsenbeschriftung))
        self.wait(0.25)
        self.play(Create(graph))
        self.wait(0.25)
        self.play(Write(funktionsterm))
        self.play(graph_ganz.animate.shift(LEFT * 2).scale(0.8), run_time=2)
        self.wait(2)

        # Punkte auf dem Graphen
        stichpunkt1 = MathTex(
            r"\text{Zwei Punkte auf}",
            r"\\",
            r"\text{der Funktion:}",
            r"\\",
            r"p_1", r"\text{ und }", r"p_2"
        )
        stichpunkt1[4].set_color(PURE_RED)
        stichpunkt1[6].set_color(PURE_RED)
        stichpunkt1.next_to(graph_ganz, RIGHT*2)

        self.play(Write(stichpunkt1), run_time=1)

        p1 = Dot(achsen.c2p(0, 0), color=PURE_RED)
        p2 = Dot(achsen.c2p(0, 0), color=PURE_RED)
        p1_beschriftung = MathTex("p_1", color=PURE_RED).next_to(p1, DOWN)

        self.play(FadeIn(p1, p1_beschriftung))
        self.play(FadeIn(p2))

        # p2 entlang des Graphen bewegen
        ursprung = achsen.c2p(0, 0)
        graph_ende = graph.point_from_proportion((1.5 - graph.t_min) / (graph.t_max - graph.t_min))

        pfad_entlang_graph = graph.get_subcurve((0 - graph.t_min) / (graph.t_max - graph.t_min), (1.5 - graph.t_min) / (graph.t_max - graph.t_min))

        kombinierter_pfad = VMobject()
        kombinierter_pfad.set_points_as_corners([ursprung])
        kombinierter_pfad.append_points(pfad_entlang_graph.get_points())

        self.play(MoveAlongPath(p2, kombinierter_pfad), run_time=2)

        p2_beschriftung = MathTex("p_2", color=PURE_RED).next_to(p2, UP)
        self.play(FadeIn(p2_beschriftung))

        # Vertikale Linie von p2 zur x-Achse
        vertikale_linie = DashedLine(start=p2.get_bottom(), end=achsen.c2p(1.5, 0), color=WHITE)
        self.play(Create(vertikale_linie))

        # Sekantenlinie zwischen p1 und p2
        sekantenlinie = Line(
            start=p1.get_center(), 
            end=p2.get_center(), 
            color=RED
        )
        mittelpunkt = (p1.get_center() + p2.get_center()) / 2
        richtung = p2.get_center() - p1.get_center()
        richtung /= np.linalg.norm(richtung)
        feste_länge = 8
        sekantenlinie.put_start_and_end_on(mittelpunkt - richtung * (feste_länge / 2), mittelpunkt + richtung * (feste_länge / 2))
        sekantenlinie.set_z_index(-3)

        self.play(Create(sekantenlinie))

        self.play(stichpunkt1.animate.scale(0.75).shift(UP*1.75), run_time=1)

        self.wait(2)

        # Zweiter Punkt nähert sich dem ersten Punkt
        stichpunkt2 = MathTex(
            r"p_1", r"\text{ und }", r"p_2", r"\text{ sich}",
            r"\\",
            r"\text{annähern lassen}"
        )
        stichpunkt2[0].set_color(PURE_RED)
        stichpunkt2[2].set_color(PURE_RED)
        
        stichpunkt2.next_to(stichpunkt1, DOWN)
        stichpunkt2.scale(0.75)

        self.play(Write(stichpunkt2), run_time=1)
        pfad_entlang_graph_p1 = graph.get_subcurve((0 - graph.t_min) / (graph.t_max - graph.t_min), (1.499999 - graph.t_min) / (graph.t_max - graph.t_min))

        kombinierter_pfad_p1 = VMobject()
        kombinierter_pfad_p1.set_points_as_corners([ursprung])
        kombinierter_pfad_p1.append_points(pfad_entlang_graph_p1.get_points())

        p1_beschriftung_pfad = kombinierter_pfad_p1.copy()
        p1_beschriftung_pfad.shift(DOWN * 0.5)

        # Sekantenlinie aktualisieren, während sich p1 bewegt
        def update_sekantenlinie(linie):
            start = p1.get_center()
            end = p2.get_center()
            mittelpunkt = (start + end) / 2
            richtung = end - start
            richtung /= np.linalg.norm(richtung)
            feste_länge = 8
            linie.put_start_and_end_on(mittelpunkt - richtung * (feste_länge / 2), mittelpunkt + richtung * (feste_länge / 2))

        sekantenlinie.add_updater(update_sekantenlinie)

        self.play(FadeOut(vertikale_linie))
        self.play(
            MoveAlongPath(p1, kombinierter_pfad_p1), 
            MoveAlongPath(p1_beschriftung, p1_beschriftung_pfad),
            run_time=2
        )

        sekantenlinie.remove_updater(update_sekantenlinie)

        tangente = sekantenlinie.copy()
        
        self.play(Transform(sekantenlinie, tangente), run_time=0.001)

        self.wait(1)

        self.play(funktionsterm.animate.shift(UP*1.5 + LEFT*3), run_time=0.5)

        # Steigungsdreieck an der Tangente
        x0 = 1.5
        h = 0.5
        x1 = x0 + h
        y0 = 0.5 * x0**2
        y1 = 0.5 * x0**2 + (x1 - x0) * x0

        # Punkte des Steigungsdreiecks
        p3 = Dot(achsen.c2p(x1, y0), color=BLUE)
        p4 = Dot(achsen.c2p(x1, y1), color=BLUE)

        # Linien des Steigungsdreiecks
        horizontale_linie = DashedLine(start=p2.get_center(), end=p3.get_center(), color=WHITE)
        vertikale_linie = DashedLine(start=p3.get_center(), end=p4.get_center(), color=WHITE)
        horizontale_linie.set_z_index(-1)
        vertikale_linie.set_z_index(-1)

        self.play(FadeIn(p3), FadeIn(p4))
        self.play(Create(horizontale_linie), Create(vertikale_linie))

        # Steigungsdreieck beschriften
        delta_x = MathTex(r"x_1", color=BLUE).next_to(horizontale_linie, DOWN)
        delta_y = MathTex(r"y_1", color=BLUE).next_to(vertikale_linie, RIGHT)

        self.play(Write(delta_x), Write(delta_y))

        # Steigungsdreieck Formel
        stichpunkt3 = MathTex(
            r"\text{Steigung} =", r"\frac{y_1}{x_1}",  r"= \lim_{h \to 0}",
            r"\\",
            r"=", r"\frac{f(x_0 + h) - f(x_0)}{h}",
        )
        stichpunkt3[5].set_color(BLUE)
        stichpunkt3.next_to(stichpunkt2, DOWN)
        stichpunkt3.scale(0.75)

        self.play(Write(stichpunkt3))

        self.wait(2)

        # Elemente ausblenden
        self.play(
            FadeOut(tangente),
            FadeOut(p1),
            FadeOut(p1_beschriftung),
            FadeOut(p2),
            FadeOut(p2_beschriftung),
            FadeOut(p3),
            FadeOut(p4),
            FadeOut(sekantenlinie),
            FadeOut(horizontale_linie),
            FadeOut(vertikale_linie),
            FadeOut(stichpunkt1),
            FadeOut(stichpunkt2),
            FadeOut(stichpunkt3),
            FadeOut(delta_x),
            FadeOut(delta_y),
            run_time=2
        )

        # Ableiten der FUnktion, Ableitungsregeln
        self.play(funktionsterm.animate.shift(UP, LEFT))

        _funktionsterm = MathTex(r"f'(x) = \frac{1}{2} \cdot 2x^{2-1} = x", color=GOLD)
        _funktionsterm.set_color(RED)
        _funktionsterm.scale(0.75)
        _funktionsterm.next_to(funktionsterm, DOWN*0.5)

        # Terme = VGroup(funktionsterm, _funktionsterm)
        # Terme.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        # Terme.shift(LEFT)

        ableitung = achsen.plot(lambda x: x, color=RED)
        
        _stichpunkt1 = MathTex(
            r"\text{Die Ableitung}", r"\text{ f' }", r"\text{der Funktion}", r"\text{ f}",
            r"\\",
            r"\text{ist die Steigung der Tangente und}",
            r"\\",
            r"\text{damit der Funktion}", r"\text{ an jedem Punkt}", r"."
        )
        _stichpunkt1[1].set_color(RED)
        _stichpunkt1[3].set_color(GOLD)
        _stichpunkt1[8].set_color(PURE_RED)
        _stichpunkt1.scale(0.5)
        _stichpunkt1.next_to(graph_ganz, RIGHT*2)
        _stichpunkt1.shift(UP*1.85, LEFT*0.3)

        self.play(Create(ableitung), 
                Write(_funktionsterm),
                Write(_stichpunkt1),
                run_time=2
                )

        """
        1. Strich unter _stichpunkt1
        2. Somit gilt für jede Funktion
        3. "Allg." Ableitungsregel definieren und einblenden 
        """

        self.wait(2)
from manim import *

class Extremata(Scene):

    def f_strich(self, x):
        return 3*x**2 + 2*x

    def tangente(self, x0):
        slope = self.f_strich(x0)
        return lambda x: slope * (x - x0) + (x0**3 + x0**2)

    def construct(self):
        # Titel
        titel = Text("Extremstellen", font="Georgia", font_size=96) 
        titel.move_to(ORIGIN)
        self.play(titel.animate.scale(0.65).shift(UP*3.1), run_time=2)
        self.wait(1)

        achsen = Axes(
            x_range=[-1.5, 0.875],
            y_range=[-0.5, 0.5],
            axis_config={"color": WHITE},
            x_axis_config={"tick_size": 0.1, "unit_size": 0.5},
            y_axis_config={"tick_size": 0.1, "unit_size": 0.5},
        )
        achsenbeschriftung = achsen.get_axis_labels(x_label="x", y_label="y", )
        achsen.add_coordinates()

        funktion = achsen.plot(lambda x: x**3 + x**2, x_range=[-1.25, 0.625], color=GOLD)

        funktionsterm = MathTex("f(x) = x^3 + x^2", color=GOLD)
        funktionsterm.next_to(funktion, LEFT)
        funktionsterm.shift(UP*2).shift(RIGHT*4)

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
        p1 = Dot(achsen.c2p(-1.25, (-1.25)**3 + (-1.25)**2), color=PURE_RED)
        p1_beschriftung = MathTex("p_1", color=PURE_RED)
        tangente_p1 = achsen.plot(self.tangente(achsen.p2c(p1.get_center()[0])[0]), x_range=[-1.5, 0.8], color=PURE_RED)
        p1_ges = VGroup(p1, p1_beschriftung, tangente_p1)
        
        p2 = Dot(achsen.c2p(0.625, 0.625**3 + 0.625**2), color=PURE_RED)
        p2_beschriftung = MathTex("p_2", color=PURE_RED)
        tangente_p2 = achsen.plot(self.tangente(achsen.p2c(p2.get_center()[0])[0]), x_range=[-1.5, 0.8], color=PURE_RED)
        p2_ges = VGroup(p2, p2_beschriftung, tangente_p2)

        ursprung_l = achsen.c2p(-1.25, (-1.25)**3 + (-1.25)**2)
        ursprung_r = achsen.c2p(0.625, 0.625**3 + 0.625**2)

        pfad_l = funktion.get_subcurve((-1.25 - funktion.t_min) / (funktion.t_max - funktion.t_min), (-(2/3) - funktion.t_min) / (funktion.t_max - funktion.t_min))
        pfad_r = funktion.get_subcurve((0 - funktion.t_min) / (funktion.t_max - funktion.t_min), (0.625 - funktion.t_min) / (funktion.t_max - funktion.t_min))

        kombinierter_pf_l = VMobject()
        kombinierter_pf_l.set_points_as_corners([ursprung_l])
        kombinierter_pf_l.append_points(pfad_l.get_points())

        kombinierter_pf_r = VMobject()
        kombinierter_pf_r.set_points_as_corners([ursprung_r])
        kombinierter_pf_r.append_points(pfad_r.get_points()).reverse_points()
        kombinierter_pf_r.append_points(achsen.c2p(0, 0))

        self.play(Create(p1), Create(p2), run_time=1.5)
        self.play(MoveAlongPath(p1, kombinierter_pf_l), MoveAlongPath(p2, kombinierter_pf_r), run_time=2)

        p1_beschriftung.next_to(p1, UP)
        p2_beschriftung.next_to(p2, (UP + RIGHT * 0.5))
        self.play(Write(p1_beschriftung), Write(p2_beschriftung), run_time=0.5)
        
        stichpunkt_1 = BulletedList(MathTex("Steigung im Punkt p_1: f'(p_1) = 0", color=WHITE), MathTex("Steigung im Punkt p_2: f'(p_2) = 0", color=WHITE)) # TODO: p_1 und p_2 rot machen, stichpunkte fertig implementieren

        tangente_p1 = achsen.plot(self.tangente(achsen.p2c(p1.get_center()[0])[0]), x_range=[-1.5, 0.8], color=PURE_RED)
        tangente_p2 = achsen.plot(self.tangente(achsen.p2c(p2.get_center()[0])[0]), x_range=[-1.5, 0.8], color=PURE_RED)

        self.play(GrowFromCenter(tangente_p1), GrowFromCenter(tangente_p2), run_time=1)
        self.wait(1)
        self.play(ShrinkToCenter(tangente_p1), ShrinkToCenter(tangente_p2), run_time=1)

        self.wait(2)
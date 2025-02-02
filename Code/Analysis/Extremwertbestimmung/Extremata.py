from manim import *

class Extremata(Scene):

    def f_strich(self, x):
        # Ableitung der Funktion f(x) = x^3 + x^2
        return 3*x**2 + 2*x

    def tangente(self, x0):
        # Berechnet die Tangente an der Stelle x0
        slope = self.f_strich(x0)
        return lambda x: slope * (x - x0) + (x0**3 + x0**2)

    def construct(self):

        speed = 0.25

        # Titel
        titel = Text("Extremstellen", font="Georgia", font_size=96) 
        titel.move_to(ORIGIN)
        self.play(titel.animate.scale(0.65).shift(UP*3.1), run_time=2)
        self.wait(1)

        # Achsen erstellen
        achsen = Axes(
            x_range=[-1.5, 0.875],
            y_range=[-0.5, 0.5],
            axis_config={"color": WHITE},
            x_axis_config={"tick_size": 0.1, "unit_size": 0.5},
            y_axis_config={"tick_size": 0.1, "unit_size": 0.5},
        )
        achsenbeschriftung = achsen.get_axis_labels(x_label="x", y_label="y")
        achsen.add_coordinates()

        # Funktion plotten
        funktion = achsen.plot(lambda x: x**3 + x**2, x_range=[-1.25, 0.625], color=GOLD)
        Ableitung = achsen.plot(lambda x: 3*x**2 + 2*x, x_range=[-0.75, 0.2], color=GOLD_E)

        # Funktionsterm anzeigen
        funktionsterm = MathTex("f(x) = x^3 + x^2", color=GOLD)
        funktionsterm.next_to(funktion, LEFT)
        funktionsterm.shift(UP*2).shift(RIGHT*4)

        # Ableitung anzeigen
        abgl_term = MathTex("f'(x) = 3x^2 + 2x", color=GOLD_E)
        abgl_term.next_to(funktionsterm, DOWN)

        graph_ganz = VGroup(achsen, achsenbeschriftung, funktion, funktionsterm, Ableitung, abgl_term)
        graph_ganz.scale(0.95).shift(DOWN*0.75)

        # Achsen und Graph animieren
        self.play(Create(achsen))
        self.wait(speed)
        self.play(Write(achsenbeschriftung))
        self.wait(speed)
        self.play(Create(funktion))
        self.wait(speed)
        self.play(Write(funktionsterm))
        self.wait(speed)
        self.play(Write(abgl_term))
        self.wait(speed)
        self.play(Create(Ableitung))
        self.wait(speed)
        self.play(graph_ganz.animate.shift(LEFT * 2).scale(0.8), run_time=2)
        self.wait(1)

        # Extremstellen
        p1 = Dot(achsen.c2p(-1.25, (-1.25)**3 + (-1.25)**2), color=BLUE_E)
        p1_beschriftung = MathTex("p_1", color=BLUE_E)
        tangente_p1 = achsen.plot(self.tangente(achsen.p2c(p1.get_center()[0])[0]), x_range=[-1.5, 0.8], color=BLUE_E)
        p1_ges = VGroup(p1, p1_beschriftung, tangente_p1)
        
        p2 = Dot(achsen.c2p(0.625, 0.625**3 + 0.625**2), color=RED_E)
        p2_beschriftung = MathTex("p_2", color=RED_E)
        tangente_p2 = achsen.plot(self.tangente(achsen.p2c(p2.get_center()[0])[0]), x_range=[-1.5, 0.8], color=RED_E)
        p2_ges = VGroup(p2, p2_beschriftung, tangente_p2)

        # Pfade für die Animation der Punkte
        ursprung_l = achsen.c2p(-1.25, (-1.25)**3 + (-1.25)**2)
        ursprung_r = achsen.c2p(0.625, 0.625**3 + 0.625**2)

        pfad_l = funktion.get_subcurve((-1.25 - funktion.t_min) / (funktion.t_max - funktion.t_min), (-(2/3) - funktion.t_min) / (funktion.t_max - funktion.t_min))
        pfad_l_punkte = pfad_l.get_points()[:-1]
        endpunkt = achsen.c2p(-2/3, (-2/3)**3 + (-2/3)**2)
        pfad_l_punkte = np.vstack([pfad_l_punkte, endpunkt])
        kombinierter_pf_l = VMobject()
        kombinierter_pf_l.set_points_as_corners([ursprung_l])
        kombinierter_pf_l.append_points(pfad_l_punkte)

        pfad_r = funktion.get_subcurve((0 - funktion.t_min) / (funktion.t_max - funktion.t_min), (0.625 - funktion.t_min) / (funktion.t_max - funktion.t_min))
        pfad_r = pfad_r.reverse_points()
        pfad_r_punkte = pfad_r.get_points()[:-1]
        endpunkt_r = achsen.c2p(0, 0)
        pfad_r_punkte = np.vstack([pfad_r_punkte, endpunkt_r])
        kombinierter_pf_r = VMobject()
        kombinierter_pf_r.set_points_as_corners([ursprung_r])
        kombinierter_pf_r.append_points(pfad_r_punkte)

        # Punkte und Pfade animieren
        self.play(Create(p1), Create(p2), run_time=1.5)
        self.play(MoveAlongPath(p1, kombinierter_pf_l), MoveAlongPath(p2, kombinierter_pf_r), run_time=2)

        p1_beschriftung.next_to(p1, DOWN * 0.55).scale(0.8)
        p2_beschriftung.next_to(p2, (UP * 0.55 + RIGHT * 0.5)).scale(0.8)
        self.play(Write(p1_beschriftung), Write(p2_beschriftung), run_time=0.5)
        
        # Stichpunkte anzeigen
        stichpunkt_1 = Text("Allgemein gilt: ", color=WHITE).scale(0.5)
        stichpunkt_1_1 = BulletedList("Steigung im Punkt $p_1$: $f'(p_1)$ = 0", color=WHITE).scale(0.5)
        stichpunkt_1_2 = BulletedList("Steigung im Punkt $p_2$: $f'(p_2)$ = 0", color=WHITE).scale(0.5)
        stichpunkt_2 = Text("Unterschiedliche Arten von\nExtremstellen:", color=WHITE).scale(0.5)
        stichpunkt_2_2_1 = BulletedList("Hochpunkt $p_1$", color=WHITE).scale(0.6)
        stichpunkt_2_2_2 = BulletedList("Tiefpunkt $p_2$", color=WHITE).scale(0.6)
        stichpunkt_1_1[0][16:18].set_color(BLUE_E) # zählt: (Leer-)Zeichen, unterstufige Zeichen, vermutl. Exponenten -- Zählt nicht: _ oder $
        stichpunkt_1_1[0][22:24].set_color(BLUE_E)
        stichpunkt_1_2[0][16:18].set_color(RED_E)
        stichpunkt_1_2[0][22:24].set_color(RED_E)
        stichpunkt_2_2_1[0][10:13].set_color(BLUE_E)
        stichpunkt_2_2_2[0][10:13].set_color(RED_E)
        stichpunkte = VGroup(stichpunkt_1, stichpunkt_1_1, stichpunkt_1_2, stichpunkt_2, stichpunkt_2_2_1, stichpunkt_2_2_2)
        stichpunkte.arrange(DOWN, aligned_edge=LEFT).next_to(graph_ganz, RIGHT, buff=0.2) # someone tell him about scale_to_fit_width() ￣へ￣

        self.play(Write(stichpunkt_1), run_time=0.25)
        self.wait(speed)

        tangente_p1 = achsen.plot(self.tangente(achsen.p2c(p1.get_center()[0])[0]), x_range=[-1.5, 0.8], color=BLUE_E)
        tangente_p2 = achsen.plot(self.tangente(achsen.p2c(p2.get_center()[0])[0]), x_range=[-1.5, 0.8], color=RED_E)

        # Tangenten und Stichpunkte animieren
        self.play(GrowFromCenter(tangente_p1), GrowFromCenter(tangente_p2), Write(stichpunkt_1_1), Write(stichpunkt_1_2), run_time=2)
        self.wait(2)
        self.play(ShrinkToCenter(tangente_p1), ShrinkToCenter(tangente_p2), run_time=1)

        self.play(Write(stichpunkt_2), run_time=0.5)
        self.wait(speed)
        self.play(Write(stichpunkt_2_2_1), run_time=0.5)
        self.play(FocusOn(p1))
        self.play(Write(stichpunkt_2_2_2), run_time=0.5)
        self.play(FocusOn(p2))

        self.wait(2)
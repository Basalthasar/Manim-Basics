from manim import *
import numpy as np

config.max_files_cached = 500

class Extremata(Scene):

    def f_strich(self, x):
        # Ableitung der Funktion f(x) = x^3 + x^2
        return 3*x**2 + 2*x
    
    def _f_strich(self, x):
        # Ableitung der Funktion f(x) = -(1/4)x^3 + (3/2)x^2 + 1
        return -(3/4)*x**2 + 3*x

    def tangente(self, x0):
        # Berechnet die Tangente an der Stelle x0
        Steigung = self.f_strich(x0)
        return lambda x: Steigung * (x - x0) + (x0**3 + x0**2)
    
    def _tangente(self, x0):
        # Berechnet die Tangente an der Stelle x0
        Steigung = self._f_strich(x0)
        return lambda x: Steigung * (x - x0) + (-(1/4)*x0**3 + (3/2)*x0**2 + 1)

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

        # Funktionen plotten
        funktion = achsen.plot(lambda x: x**3 + x**2, x_range=[-1.25, 0.625], color=GOLD)
        Ableitung = achsen.plot(lambda x: 3*x**2 + 2*x, x_range=[-0.75, 0.2], color=GOLD_E)

        Ableitung_2 = achsen.plot(lambda x: 6*x + 2, x_range=[-0.4, -0.266], color=DARK_BROWN)
        Ableitung_2.set_opacity(0)

        # Funktionsterm anzeigen
        funktionsterm = MathTex("f(x) = x^3 + x^2", color=GOLD)
        funktionsterm.next_to(funktion, LEFT)
        funktionsterm.shift(UP*2).shift(RIGHT*4)

        # Ableitung anzeigen
        abgl_term = MathTex("f'(x) = 3x^2 + 2x", color=GOLD_E)
        abgl_term.next_to(funktionsterm, DOWN)

        abgl_term_2 = MathTex("f''(x) = 6x + 2", color=DARK_BROWN)
        abgl_term_2.set_opacity(0)

        graph_ganz = VGroup(achsen, achsenbeschriftung, funktion, funktionsterm, Ableitung, abgl_term, Ableitung_2, abgl_term_2) 
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

        p1_beschriftung.next_to(p1, (UP * 0.35 + RIGHT * 0.5)).scale(0.8)
        p2_beschriftung.next_to(p2, (UP * 0.55 + RIGHT * 0.5)).scale(0.8)
        self.play(Write(p1_beschriftung), Write(p2_beschriftung), run_time=0.5)
        
        # Stichpunkte anzeigen
        stichpunkt_1 = Text("Allgemein gilt: ", color=WHITE).scale(0.5)
        stichpunkt_1_1 = BulletedList("Steigung im Punkt $p_1$: $f'(p_1)$ = 0", color=WHITE).scale(0.5)
        stichpunkt_1_2 = BulletedList("Steigung im Punkt $p_2$: $f'(p_2)$ = 0", color=WHITE).scale(0.5)
        stichpunkt_2 = Text("Unterschiedliche Arten von\nExtremstellen:", color=WHITE).scale(0.5)
        stichpunkt_2_2_1 = BulletedList("Hochpunkt $p_1$", color=WHITE).scale(0.6)
        stichpunkt_2_2_2 = BulletedList("Tiefpunkt $p_2$", color=WHITE).scale(0.6)

        # Colorcoding 
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
        self.play(GrowFromPoint(tangente_p1, p1.get_center()), GrowFromPoint(tangente_p2, p2.get_center()), Write(stichpunkt_1_1), Write(stichpunkt_1_2), run_time=2)
        self.wait(2)
        self.play(ShrinkToCenter(tangente_p1), ShrinkToCenter(tangente_p2), run_time=1)

        self.play(Write(stichpunkt_2), run_time=0.5)
        self.wait(speed)
        self.play(Write(stichpunkt_2_2_1), run_time=0.5)
        self.play(FocusOn(p1))
        self.play(Write(stichpunkt_2_2_2), run_time=0.5)
        self.play(FocusOn(p2))
        
        self.wait(2)

        self.play(
            Unwrite(stichpunkt_1),
            Unwrite(stichpunkt_1_1),
            Unwrite(stichpunkt_1_2),
            Unwrite(stichpunkt_2),
            Unwrite(stichpunkt_2_2_1),
            Unwrite(stichpunkt_2_2_2),
        )
        self.wait(speed)

        # Hinreichende Bedingung für HP und TP
        # Stichpunkte
        _stichpunkt_1 = Text("Rechnerische Bestimmung\nder Art der Extremstellen").scale(0.5)
        _stichpunkt_1_1 = BulletedList("Hochpunkt: $f''(p_1) < 0$", color=WHITE).scale(0.5)
        _stichpunkt_1_2 = BulletedList("Tiefpunkt: $f''(p_2) > 0$", color=WHITE).scale(0.5)
        _stichpunkt_1_3 = BulletedList(r"Es gilt: $f''(x) \ne 0$", color=WHITE).scale(0.5)
        _stichpunkte = VGroup(_stichpunkt_1, _stichpunkt_1_1, _stichpunkt_1_2, _stichpunkt_1_3)
        _stichpunkte.arrange(DOWN, aligned_edge=LEFT).next_to(graph_ganz, RIGHT, buff=0.2)

        # Colorcoding
        _stichpunkt_1_1[0][15:17].set_color(BLUE_E)
        _stichpunkt_1_2[0][15:17].set_color(RED_E)

        # 2. Ableitung animieren
        self.play(
            funktionsterm.animate.shift(UP*0.85), 
            abgl_term.animate.shift(UP*0.85), 
            run_time=0.5
        )

        self.wait(speed)

        abgl_term_2.next_to(abgl_term, DOWN)

        for i in range(60):
            self.play(
                abgl_term_2.animate.set_opacity(i/60),
                Ableitung_2.animate.set_opacity(i/60),
                run_time=0.025
            )

        # Stichpunkte
        for stichpunkt in _stichpunkte:
            self.play(Write(stichpunkt), run_time=0.35)
            self.wait(0.35)

        self.play(
            Circumscribe(_stichpunkt_1_1[0][18:19], color=YELLOW),
            Circumscribe(_stichpunkt_1_2[0][18:19], color=YELLOW),
            run_time=1
        )

        self.wait(2)

        # Szene aufräumen
        tangente_p1.set_opacity(0)
        tangente_p2.set_opacity(0)

        self.play(
            Unwrite(_stichpunkt_1),
            Unwrite(_stichpunkt_1_1),
            Unwrite(_stichpunkt_1_2),
            Unwrite(_stichpunkt_1_3),
            run_time=2
        )

        self.wait(speed)

        self.play(
            Unwrite(funktionsterm),
            Unwrite(abgl_term),
            Unwrite(abgl_term_2),
            Uncreate(funktion),
            Uncreate(Ableitung),
            Uncreate(Ableitung_2),
            Uncreate(achsenbeschriftung),
            Uncreate(p1),
            Uncreate(p1_beschriftung),
            Uncreate(p2),
            Uncreate(p2_beschriftung),
            run_time=2
        )

        self.wait(speed)

        _achsen = Axes(
            x_range=[-0.1, 6.5],
            y_range=[-2, 9.9],
            axis_config={"color": WHITE},
        )
        _achsenbeschriftung = _achsen.get_axis_labels(x_label="x", y_label="y")

        self.play(Transform(achsen, _achsen), run_time=2)

        # -(1/4)x^3 + (3/2)x^2 + 1
        # für -0.1 <= x <= 6.5 plotten
        # also -0.1 <= y <= 9.5
        _funktion = _achsen.plot(lambda x: (-(1/4))*x**3 + (3/2)*x**2 + 1, x_range=[-0.1, 6.3], color=GOLD)
        _funktionsterm = MathTex("f(x) = -\\frac{1}{4}x^3 + \\frac{3}{2}x^2 + 1", color=GOLD)
        _funktionsterm.scale(0.5).move_to(_achsen.c2p(0.8, 8.25))

        _ableitung = _achsen.plot(lambda x: -(3/4)*x**2 + 3*x, x_range=[-0.1, 4.5], color=LIGHT_BROWN)
        _abgl_term = MathTex("f'(x) = -\\frac{3}{4}x^2 + 3x", color=LIGHT_BROWN)
        _abgl_term.scale(0.5).next_to(_funktionsterm, DOWN)

        _ableitung2 = _achsen.plot(lambda x: -(3/2)*x + 3, x_range=[-0.1, 3.25], color=ORANGE)
        _abgl_term2 = MathTex("f''(x) = -\\frac{3}{2}x + 3", color=ORANGE)
        _abgl_term2.scale(0.5).next_to(_abgl_term, DOWN)

        _ableitung3 = _achsen.plot(lambda x: -(3/2), x_range=[-0.1, 6.5], color=DARK_BROWN)
        _abgl_term3 = MathTex("f'''(x) = -\\frac{3}{2}", color=DARK_BROWN)
        _abgl_term3.scale(0.5).next_to(_abgl_term2, DOWN)

        _funktionen = VGroup(_funktion, _ableitung, _ableitung2, _ableitung3)
        _terme = VGroup(_funktionsterm, _abgl_term, _abgl_term2, _abgl_term3)

        self.wait(speed)
        self.play(Create(_achsenbeschriftung), run_time=0.5)
        self.wait(speed)
        self.play(Write(_achsen.add_coordinates()))
        
        _graph_ganz = VGroup(_achsen, _achsenbeschriftung, _funktionen, _terme)

        for i in range(4):
            self.wait(speed)
            self.play(Create(_funktionen[i]), run_time=1)
            self.wait(speed)
            self.play(Write(_terme[i]), run_time=0.5)

        self.wait(speed)
        self.remove(achsen)
        self.play(_graph_ganz.animate.shift(LEFT * 2).scale(0.8), run_time=2)

        hp = Dot(_funktion.get_point_from_function(4), color=BLUE_E)
        tangente_hp = _achsen.plot(self._tangente(_achsen.p2c(hp.get_center()[0])[0]), x_range=[-0.1, 6.5], color=BLUE_E)
        hp_Betonung = DashedLine(start=hp.get_center(), end=_achsen.c2p(4, 0), color=WHITE).set_z_index(-5)
        
        tp = Dot(_funktion.get_point_from_function(0), color=RED_E)
        tangente_tp = _achsen.plot(self._tangente(_achsen.p2c(tp.get_center()[0])[0]), x_range=[-0.1, 6.5], color=RED_E)
        tp_Betonung = DashedLine(start=tp.get_center(), end=_achsen.c2p(0, 0), color=WHITE).set_z_index(-5)

        wp = Dot(_funktion.get_point_from_function(2), color=GREEN)
        tangente_wp = _achsen.plot(self._tangente(_achsen.p2c(wp.get_center()[0])[0]), x_range=[-0.1, 3.5], color=GREEN)
        wp_Betonung = DashedLine(start=wp.get_center(), end=_achsen.c2p(2, 0), color=WHITE).set_z_index(-5)

        __stichpunkt_1 = Text("Neben den Extrempunkten \nexistiert ein weiterer \ncharakteristischer Punkt", color=WHITE)\
            .scale(0.45)\
            .next_to(_graph_ganz, RIGHT, buff=0.1)\
            .shift(UP * 1.5)
        __stichpunkt_1_2 = BulletedList("Ein sog. Wendepunkt $p_3$", color=WHITE)\
            .scale(0.6)\
            .next_to(__stichpunkt_1, DOWN, aligned_edge=LEFT)\
            .shift(RIGHT * 0.2)
        __stichpunkt_1_3 = BulletedList("Für $p_3$ gilt: $f''(p_3) = 0$", color=WHITE)\
            .scale(0.6)\
            .next_to(__stichpunkt_1_2, DOWN, aligned_edge=LEFT)\
            .shift(RIGHT * 0.4)

        __stichpunkt_2 = Text("Unterschiedliche Arten von\nWendepunkten:", color=WHITE)\
            .scale(0.45)\
            .next_to(__stichpunkt_1_3, DOWN, buff=0.3)\
            .shift(LEFT * 0.4)
        __stichpunkt_2_1 = BulletedList("Stärkste Steigung, wie in $p_3$", color=WHITE)\
            .scale(0.6)\
            .next_to(__stichpunkt_2, DOWN, aligned_edge=LEFT)\
            .shift(RIGHT * 0.2)
        __stichpunkt_2_1_2 = BulletedList("wobei gilt: $f'''(p_3) < 0$", color=WHITE)\
            .scale(0.6)\
            .next_to(__stichpunkt_2_1, DOWN, aligned_edge=LEFT)\
            .shift(RIGHT * 0.4)
        __stichpunkt_2_2 = BulletedList("Stärkstes Gefälle", color=WHITE)\
            .scale(0.6)\
            .next_to(__stichpunkt_2_1_2, DOWN, aligned_edge=LEFT)\
            .shift(LEFT * 0.4)
        __stichpunkt_2_2_2 = BulletedList("wobei gilt: $f'''(x) > 0$", color=WHITE)\
            .scale(0.6)\
            .next_to(__stichpunkt_2_2, DOWN, aligned_edge=LEFT)\
            .shift(RIGHT * 0.4)

        # Colorcoding
        __stichpunkt_1_2[0][18:20].set_color(GREEN)
        __stichpunkt_1_3[0][5:7].set_color(GREEN)
        __stichpunkt_1_3[0][16:18].set_color(GREEN)
        __stichpunkt_2_1[0][24:26].set_color(GREEN)
        __stichpunkt_2_1_2[0][16:18].set_color(GREEN)

        __stichpunkte = VGroup(__stichpunkt_1, __stichpunkt_1_2, __stichpunkt_1_3, __stichpunkt_2, __stichpunkt_2_1, __stichpunkt_2_1_2, __stichpunkt_2_2, __stichpunkt_2_2_2)

        self.wait(speed)

        self.play(Write(__stichpunkt_1))
        self.play(
            Create(hp),
            GrowFromPoint(tangente_hp, _funktion.get_point_from_function(4)),
            GrowFromEdge(hp_Betonung, _funktion.get_point_from_function(4)),
            Create(tp),
            GrowFromPoint(tangente_tp, _funktion.get_point_from_function(0)),
            GrowFromEdge(tp_Betonung, _funktion.get_point_from_function(0)),
            run_time=2
        )

        self.wait(speed)

        self.play(
            Uncreate(hp),
            Uncreate(tp),
            ShrinkToCenter(tangente_hp),
            ShrinkToCenter(tangente_tp),
            ShrinkToCenter(hp_Betonung),
            ShrinkToCenter(tp_Betonung),
            run_time=2
        )

        self.wait(speed)
        self.play(Write(__stichpunkt_1_2), Write(__stichpunkt_1_3), run_time=2)
        self.wait(speed)
        self.play(Create(wp), GrowFromPoint(tangente_wp, _funktion.get_point_from_function(2)), GrowFromEdge(wp_Betonung, _funktion.get_point_from_function(2)), run_time=2)
        self.wait(speed)
        self.play(Write(__stichpunkt_2))
        self.wait(speed)
        self.play(Write(__stichpunkt_2_1), Write(__stichpunkt_2_1_2), run_time=2)
        self.wait(speed)
        self.play(Flash(wp), run_time=2)
        self.wait(speed)
        self.play(Write(__stichpunkt_2_2), Write(__stichpunkt_2_2_2), run_time=2)
        self.wait(speed)
        self.play(Circumscribe(__stichpunkt_2_1_2[0][19:20], color=YELLOW), run_time=1)
        self.wait(speed)
        self.play(Circumscribe(__stichpunkt_2_2_2[0][18:19], color=YELLOW), run_time=1)
        self.wait(speed)

        self.wait(2)

        # Szene leeren

        self.play(
            Unwrite(__stichpunkte),
            Uncreate(wp),
            ShrinkToCenter(tangente_wp),
            ShrinkToCenter(wp_Betonung),
            Uncreate(_funktion),
            Uncreate(_ableitung),
            Uncreate(_ableitung2),
            Uncreate(_ableitung3),
            Uncreate(_funktionsterm),
            Uncreate(_abgl_term),
            Uncreate(_abgl_term2),
            Uncreate(_abgl_term3),
            Unwrite(_achsenbeschriftung),
            Uncreate(_achsen),
            run_time=3
        )

        self.wait(speed)

        self.play(titel.animate.scale(1.5384).move_to(ORIGIN), run_time=2)

        self.wait(2)
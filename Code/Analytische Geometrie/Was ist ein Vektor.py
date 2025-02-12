from manim import *

config.frame_rate = 60
config.max_files_cached = 500

class Analytische_Geometrie_t1(ThreeDScene):
    
    def Stichpunkt(self, content, size=18):
        # Stichpunkt und Inhalt
        Stichpunkt = Text("→", font_size=size)
        content = Text(content, font="Georgia", font_size=size)
        
        # Inhalt direkt neben den Stichpunkt positionieren
        content.next_to(Stichpunkt, RIGHT, buff=0.2)
        
        # Gruppiertes Resultat
        return VGroup(Stichpunkt, content)

    def construct(self):
        
        speed = 0.25

        # Titel initialisieren und anzeigen
        Titel = Text("Analytische Geometrie", font="Georgia", font_size=72) 
        self.play(Write(Titel))

        self.wait(1)

        # zentralisieren
        Titel.move_to(ORIGIN)
        self.play(Titel.animate.scale(0.75).shift(UP*2.5), run_time=2)

        self.wait(1)

        Themen_Stichpunkte = VGroup(
            self.Stichpunkt("Definition eines Vektors"),
            self.Stichpunkt("Geradengleichungen"),
            self.Stichpunkt("Lagebeziehungen mit Geraden"),
            self.Stichpunkt("Abstandsprobleme"),
            self.Stichpunkt("Ebenen"),
            self.Stichpunkt("Lagebeziehungen mit Ebenen und Geraden"),
            self.Stichpunkt("Die Hilfsebene zur Abstandsbestimmung"),
            self.Stichpunkt("Das Kreuzprodukt"),
            self.Stichpunkt("Das Spatprodukt"),
            self.Stichpunkt("Die Hessesche Normalform"),
            self.Stichpunkt("Geraden- und Ebenenscharen")
        ).arrange(DOWN, buff=0.25).shift(DOWN*0.8)

        self.play(Write(Themen_Stichpunkte), run_time=7.5)

        self.wait(2)

        self.play(
            Titel.animate.shift(UP).set_opacity(0),
            Themen_Stichpunkte[0].animate.move_to(UP*3).scale(4),
            *[FadeOut(sp, shift=DOWN) for sp in Themen_Stichpunkte[1:]],
            run_time=1.5
        )

        achsen = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=4,
        ).shift(DOWN).scale(1.25)

        achsen3d = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=4,
            y_length=4,
            z_length=4
        ).shift(DOWN).scale(1.25)

        achsen.add_coordinates(font_size=25)
        achsen3d.add_coordinates(font_size=25).set_z_index(-5)

        # Labels der Achsen
        x_label = achsen.get_x_axis_label(Tex("x"))
        x_label3d = achsen3d.get_x_axis_label(Tex("x"))
        y_label = achsen.get_y_axis_label(Tex("y"))
        y_label3d = achsen3d.get_y_axis_label(Tex("y"))
        z_label3d = achsen3d.get_z_axis_label(Tex("z"))

        # Vektoren
        vektor_x = Arrow3D(achsen.c2p(0, 0, 0), achsen.c2p(1, 0, 0), color=RED)
        vektor_x3d = Arrow3D(achsen3d.c2p(0, 0, 0), achsen3d.c2p(1, 0, 0), color=RED)
        vektor_y = Arrow3D(achsen.c2p(1, 0, 0), achsen.c2p(1, 1, 0), color=GREEN)
        vektor_y3d = Arrow3D(achsen3d.c2p(1, 0, 0), achsen3d.c2p(1, 1, 0), color=GREEN)
        vektor_z = Arrow3D(achsen.c2p(1, 1, 0), achsen.c2p(1, 1, 1), color=BLUE)
        vektor_z3d = Arrow3D(achsen3d.c2p(1, 1, 0), achsen3d.c2p(1, 1, 1), color=BLUE)

        # Punkt
        p_1 = Dot3D(point=achsen.c2p(1, 1, 1), color=YELLOW)
        p_13d = Dot3D(point=achsen3d.c2p(1, 1, 1), color=YELLOW)
        p_1_m = Dot3D(point=achsen.c2p(0, 0, 0), color=YELLOW_A).set_opacity(0)
        p_1_m3d = Dot3D(point=achsen3d.c2p(1, 1, 0), color=YELLOW_A).set_opacity(0)
        p_1_beschriftung = MathTex("p_1", font_size=25, color=YELLOW).next_to(p_1, RIGHT, buff=0.1)
        p_1_beschriftung3d = MathTex("p_1", font_size=25, color=YELLOW).next_to(p_13d, RIGHT, buff=0.1).rotate(PI/2, axis=RIGHT)

        graph_ganz = VGroup(achsen, x_label, y_label, vektor_x, vektor_y, vektor_z, p_1, p_1_m, p_1_beschriftung)

        # Animation
        self.play(
            Create(achsen),
            Write(x_label),
            Write(y_label),
            run_time=2
        )

        self.play(GrowFromPoint(vektor_x, achsen.c2p(0, 0, 0)))
        self.play(GrowFromPoint(vektor_y, achsen.c2p(1, 0, 0)))
        vektor_z.set_opacity(0) 
        self.play(GrowFromPoint(vektor_z, achsen.c2p(1, 1, 0)))
        self.play(Create(p_1), Write(p_1_beschriftung))
        self.wait(speed)
        self.play(graph_ganz.animate.move_to(LEFT * 4.25 + DOWN * 0.8), run_time=2)

        # Einführung: Text
        Stichpunkt_1 = Tex("Um zum Punkt $p_1 (1|1)$ zu gelangen\\\\ gilt in einem (2d) Koordinatensystem:").scale(0.95)
        Stichpunkt_1_1 = BulletedList("Eine Längeneinheit in die x-Richtung gehen", "und eine weitere Längeneinheit in die y-Richtung").scale(0.65)

        # Positionierung
        Stichpunkte = VGroup(Stichpunkt_1, Stichpunkt_1_1).arrange(DOWN, buff=0.25, aligned_edge=LEFT).next_to(achsen, RIGHT, buff=0.5).shift(UP)
        Stichpunkt_1_1.shift(RIGHT * 0.25)

        # Colorcoding
        Stichpunkt_1[0][10:12].set_color(YELLOW)
        Stichpunkt_1_1[0][1:500].set_color(RED)
        Stichpunkt_1_1[1][4:500].set_color(GREEN)

        vektor_x_path = ParametricFunction(
            lambda t: achsen.c2p(0, 0, 0) + t*(achsen.c2p(1, 0, 0) - achsen.c2p(0, 0, 0)),
            t_range=[0, 1],
            color=RED
        )

        vektor_y_path = ParametricFunction(
            lambda t: achsen.c2p(1, 0, 0) + t*(achsen.c2p(1, 1, 0) - achsen.c2p(1, 0, 0)),
            t_range=[0, 1],
            color=GREEN
        )

        vektor_z_path = ParametricFunction(
            lambda t: achsen.c2p(1, 1, 0) + t*(achsen.c2p(1, 1, 1) - achsen.c2p(1, 1, 0)),
            t_range=[0, 1],
            color=BLUE
        )

        self.play(Write(Stichpunkt_1), run_time=2)
        self.wait(speed)
        self.play(p_1_m.animate.set_opacity(1))
        self.wait(speed)
        self.play(Write(Stichpunkt_1_1[0]), MoveAlongPath(p_1_m, vektor_x_path), run_time=2)
        self.wait(speed)
        self.play(Write(Stichpunkt_1_1[1]), MoveAlongPath(p_1_m, vektor_y_path), run_time=2)
        self.wait(speed)

        self.wait(2)

        self.play(
            Unwrite(Stichpunkte),
            Unwrite(Themen_Stichpunkte[0]),
            run_time=1
        )

        self.move_camera(phi=45*DEGREES, theta=45*DEGREES, zoom=0.75, run_time=1.5)

        self.play(
            ReplacementTransform(p_1_beschriftung, p_1_beschriftung3d),
            ReplacementTransform(x_label, x_label3d),
            ReplacementTransform(y_label, y_label3d),
            Write(z_label3d),
            ReplacementTransform(achsen, achsen3d),
            ReplacementTransform(vektor_x, vektor_x3d),
            ReplacementTransform(vektor_y, vektor_y3d),
            ReplacementTransform(p_1, p_13d),
            ReplacementTransform(p_1_m, p_1_m3d),
            Uncreate(vektor_z),
            GrowFromPoint(vektor_z3d, achsen3d.c2p(1, 1, 0)),
            run_time=3
        )
        achsen.set_opacity(0)

        graph_ganz3d = VGroup(achsen3d, x_label3d, y_label3d, z_label3d, vektor_x3d, vektor_y3d, vektor_z3d, p_13d, p_1_m3d, p_1_beschriftung3d)

        self.play(graph_ganz3d.animate.scale(2).move_to(RIGHT * 2.5 + DOWN * 3), run_time=1)

        self.wait(speed)

        Stichpunkt_2 = Tex("Erweitert man das Koordinatensystem\\\\um eine weitere Dimension...").scale(0.75)
        Stichpunkt_2_1 = BulletedList("muss man eine weitere LE in die z-Richtung gehen").scale(0.55)
        Stichpunkt_2_2 = Tex("Der Punkt $p_1 (1|1|1)$ wird erreicht.").scale(0.75)
        
        Stichpunkt_2_1[0][8:500].set_color(BLUE)
        Stichpunkt_2_2[0][11].set_color(RED); Stichpunkt_2_2[0][13].set_color(GREEN); Stichpunkt_2_2[0][15].set_color(BLUE)

        Stichpunkte_3d = VGroup(Stichpunkt_2, Stichpunkt_2_1, Stichpunkt_2_2).arrange(DOWN, buff=0.25, aligned_edge=LEFT)

        self.add_fixed_in_frame_mobjects(Stichpunkte_3d) # Aus welcher Ecke der Dokumentation das auch immer gekrochen ist...

        Stichpunkte_3d.to_corner(UR).shift(DOWN * 0.25 + LEFT * 0.25)
        Stichpunkt_2_1.shift(RIGHT * 0.25)
        

        self.play(Write(Stichpunkte_3d))
        
        # p_1_m3d bewegen

        self.wait(2)
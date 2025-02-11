from manim import *

config.frame_rate = 60
config.max_files_cached = 500

class Analytische_Geometrie_t1(Scene):

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

        Stichpunkte = VGroup(
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

        self.play(Write(Stichpunkte), run_time=7.5)

        self.wait(2)

        self.play(
            Titel.animate.shift(UP).set_opacity(0),
            Stichpunkte[0].animate.move_to(UP*3).scale(4),
            *[FadeOut(sp, shift=DOWN) for sp in Stichpunkte[1:]],
            run_time=1.5
        )

        achsen = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=4,
            y_length=4,
            z_length=4
        ).shift(DOWN).scale(1.25)

        achsen.add_coordinates(font_size=25)

        # Labels der Achsen
        x_label = achsen.get_x_axis_label(Tex("x"))
        y_label = achsen.get_y_axis_label(Tex("y"))
        z_label = achsen.get_z_axis_label(Tex("z"))

        # Vektoren
        vektor_x = Arrow3D(achsen.c2p(0, 0, 0), achsen.c2p(1, 0, 0), color=RED)
        vektor_y = Arrow3D(achsen.c2p(1, 0, 0), achsen.c2p(1, 1, 0), color=GREEN)
        vektor_z = Arrow3D(achsen.c2p(1, 1, 0), achsen.c2p(1, 1, 1), color=BLUE)

        # Punkt
        p_1 = Dot3D(point=achsen.c2p(1, 1, 1), color=YELLOW)
        p_1_m = Dot3D(point=achsen.c2p(0, 0, 0), color=YELLOW_A).set_opacity(0)
        p_1_beschriftung = MathTex("p_1", font_size=25, color=YELLOW).next_to(p_1, RIGHT, buff=0.1)

        graph_ganz = VGroup(achsen, x_label, y_label, z_label, vektor_x, vektor_y, vektor_z, p_1, p_1_m, p_1_beschriftung)

        # Animation
        self.play(
            Create(achsen),
            Write(x_label),
            Write(y_label),
            Write(z_label),
            run_time=2
        )

        self.play(GrowFromPoint(vektor_x, achsen.c2p(0, 0, 0)))
        self.play(GrowFromPoint(vektor_y, achsen.c2p(1, 0, 0)))
        self.play(GrowFromPoint(vektor_z, achsen.c2p(1, 1, 0)))
        self.play(Create(p_1), Write(p_1_beschriftung))
        self.wait(speed)
        self.play(graph_ganz.animate.move_to(LEFT * 4.25 + DOWN * 0.8), run_time=2)

        # Einführung: Text
        Stichpunkt_1 = Tex("Um zum Punkt $p_1 (1|1)$ zu gelangen")
        Stichpunkt_1_1 = BulletedList("muss man vom Ursprung 1 LE in die x-Richtung gehen", "eine weitere LE in die y-Richtung").scale(0.65)

        # Positionierung
        Stichpunkte = VGroup(Stichpunkt_1, Stichpunkt_1_1).arrange(DOWN, buff=0.25).next_to(achsen, RIGHT, buff=0.25).shift(UP*2.5)
        Stichpunkt_1_1.move_to(RIGHT * 0.25) # FIXME: indent

        # Colorcoding
        Stichpunkt_1[0][10:12].set_color(YELLOW)
        Stichpunkt_1_1[0][19:37].set_color(RED)
        Stichpunkt_1_1[1][1:500].set_color(GREEN)

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

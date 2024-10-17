from manim import *

class Obj_im_Raum(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        # Labels der Achsen
        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8)
        z_label = axes.get_z_axis_label(Tex("z"))

        # Der eingezeichnete Vektor [1, 1, 1]
        vector = Arrow3D([0, 0, 0], [1, 1, 1], color=GREEN_D)

        # Der Punkt, der sich bewegt
        punkt = Dot3D(point=[0, 0, 0], color=GREEN_B)
        Bewegung = punkt.animate.move_to([1, 1, 1])

        # Ebene: Verschobene Ebene durch (1, 1, 1) orthogonal zu [1, 1, 1]
        ebene_kf = lambda x, y: 1 - x - y  # Ebenengleichung: x + y + z = 3
        Ebene = Surface(
            lambda u, v: axes.c2p(u + 1, v + 1, ebene_kf(u, v) + 1),  # Ursprung in (1, 1, 1)
            u_range=[-1.5, 1.5],  # Breite der Ebene auf 3 Einheiten in jede Richtung
            v_range=[-1.5, 1.5],
            stroke_color=GREEN_A,
            fill_color=GREEN_A,
            fill_opacity=0.75,
            checkerboard_colors=[GREEN_A, GREEN_E]
        ).move_to(axes.c2p(1, 1, 1))

        # Kamera herauszoomen, um Achsen zu sehen
        self.set_camera_orientation(zoom=0.5)

        # Achsen und Labels in Szene einfügen
        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label))

        self.wait(0.5)

        # Kameraeinstellung anpassen
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)

        self.wait(0.5)

        # Vektor animieren
        self.play(Create(vector))

        self.wait(0.5)

        # Punkt hinzufügen und animieren
        self.add(punkt)

        self.wait(0.2)

        # Punkt bewegt sich zu (1, 1, 1)
        self.play(Bewegung)
        
        # Ebene wächst aus dem Mittelpunkt
        self.play(GrowFromCenter(Ebene))

        self.wait(0.5)

        # Kamera drehen
        self.begin_ambient_camera_rotation(rate=0.375) 

        self.wait(5)

        # Drehung stoppen
        self.stop_ambient_camera_rotation()

        self.wait(2)

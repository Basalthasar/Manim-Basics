from manim import *

class title_raw(Scene):
    def construct(self):

        # Titel initialisieren
        Titel = Text("Titel", font="Georgia", font_size=96) 
        
        # zentralisieren
        Titel.move_to(ORIGIN)

        self.play(
            Titel.animate.scale(0.75).shift(UP*2.5),
            run_time=3
        )

        self.wait(1)
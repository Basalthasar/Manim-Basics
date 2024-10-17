from manim import *

class Analytische_Geometrie_t1(Scene):
    def construct(self):
        # Titel initialisieren und anzeigen
        Titel = Text("Analytische Geometrie1", font="Georgia", font_size=72) 
        self.play(Write(Titel))

        self.wait(1)

        # zentralisieren
        Titel.move_to(ORIGIN)
        self.play(Titel.animate.scale(0.75).shift(UP*2.5), run_time=2)

        self.wait(1)

        # Stichpunkte gruppieren und anzeigen
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

        self.wait(1)

    def Stichpunkt(self, content, size=18):
        # Stichpunkt und Inhalt
        Stichpunkt = Text("→", font_size=size)
        content = Text(content, font="Georgia", font_size=size)
        
        # Inhalt direkt neben den Stichpunkt positionieren
        content.next_to(Stichpunkt, RIGHT, buff=0.2)
        
        # Gruppiertes Resultat
        return VGroup(Stichpunkt, content)

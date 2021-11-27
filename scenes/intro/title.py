from manim import *


class Title(Scene):
    def construct(self):
        title = Tex("But what are Polya vector fields?", color=GOLD_B).shift(UP * 0.7)

        title.scale(1.25)

        complex = Tex("Math 126: Complex Analysis", color=RED_B)

        complex.next_to(title, DOWN)

        complex.scale(0.8)

        authors = Tex("Alex Brown, Will Chen", color=BLUE_B)

        authors.next_to(complex, DOWN)

        authors.scale(0.6)

        self.play(Write(title))
        self.wait(3)
        self.play(Write(complex))
        self.wait(1)
        self.play(Write(authors))
        self.wait(2)

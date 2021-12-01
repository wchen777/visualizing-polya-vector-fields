from manim import *


class Title(Scene):
    def construct(self):
        title = Tex(r"But what \textit{are} Polya vector fields?").shift(UP * 0.7).set_color_by_gradient(RED_B, GOLD_B)

        title.scale(1.25)

        complex = Tex("Math 126: Complex Analysis").set_color_by_gradient(PURPLE_C, MAROON_C)

        complex.next_to(title, DOWN)

        complex.scale(0.8)

        authors = Tex("Alex Brown, Will Chen").set_color_by_gradient(BLUE_C, GREEN_C)

        authors.next_to(complex, DOWN)

        authors.scale(0.6)

        self.play(Write(title))
        self.wait(3)
        self.play(Write(complex))
        self.wait(1)
        self.play(Write(authors))
        self.wait(2)

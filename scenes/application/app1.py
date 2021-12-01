from manim import *


class AppTitle(Scene):
    def construct(self):
        title = Tex("Applications of Polya vector fields").shift(UP * 0.5).set_color_by_gradient(GOLD_C, MAROON_D)

        title.scale(1.25)

        self.play(Write(title))
        self.wait(5)

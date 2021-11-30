from manim import *


class AppTitle(Scene):
    def construct(self):
        title = Tex("Applications of Polya vector fields", color=MAROON_B).shift(UP * 0.7)

        title.scale(1.25)

        self.play(Write(title))
        self.wait(5)

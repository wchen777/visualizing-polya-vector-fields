from manim import *


class Winding4(Scene):
    def construct(self):
        title = Title("Winding numbers as flux", color=BLUE_B)

        self.play(Write(title, run_time=1.5))

        self.wait(8)

        t1 = Tex(r"$\oint_{L} \frac{1}{z} dz = 2\pi i \cdot $ (\# of winding numbers of $L$ around the origin)",
                 color=GREEN_B).shift(UP * 1)

        t1.scale(0.85)

        t2 = Tex(r"$\oint_{L} \frac{1}{z} dz = \text{Work}\left[ \frac{1}{\boldsymbol{\overline{z}}}, L \right] "
                 r"+ i \cdot \text{Flux}\left[ \frac{1}{\boldsymbol{\overline{z}}}, L \right]$",
                 color=GOLD_B).shift(DOWN * 1)

        t2.scale(0.85)

        self.play(Write(t1, run_time=2))

        self.wait(10)

        self.play(Write(t2, run_time=2))

        self.wait(15)


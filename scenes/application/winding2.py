from manim import *


class Winding2(Scene):
    def construct(self):
        title = Title("Area as flux", color=BLUE_B)

        self.play(Write(title, run_time=1.5))

        self.wait(8)

        t1 = Tex(r"$\int_{C} \bar{z} dz = 2iA$",
                 color=TEAL_A).shift(UP * 1.75)

        t1.scale(0.75)

        t2 = Tex(r"More formally, for a function $f(z) = u(x + iy) + iv(x + iy)$, we define the Polya vector field to be:",
                 color=GREEN_A)

        t2.next_to(t1, DOWN)

        t2.scale(0.75)

        t3 = Tex(r"$\overline{\mathbf{f}(x, y)} = (u(x, y), -v(x, y))$",
                 color=RED_A).shift(DOWN* 0.5)

        t3.scale(0.75)


        self.play(Write(t1, run_time=2))

        self.wait(15)

        self.play(Write(t2, run_time=2))

        self.play(Write(t3, run_time=2))

        self.wait(15)


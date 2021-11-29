from manim import *


class Int1(Scene):
    def construct(self):
        title = Title("Polya vector fields of analytic functions", color=BLUE_B)

        self.play(Write(title, run_time=1.5))

        self.wait(2)

        t1 = Tex(r"We've now defined a visual intuition for complex integration. But let's pose another question:",
                 color=TEAL_A).shift(UP * 1)

        t1.scale(0.75)

        t2 = Tex(r"{\bf Given a Pólya vector field, how can we tell whether or not $f$ is analytic?}",
                 color=RED_B)

        t2.next_to(t1, DOWN)

        t2.scale(0.75)

        self.play(Write(t1, run_time=2))

        self.wait(6)

        self.play(Write(t2, run_time=2))

        self.wait(10)
from manim import *


class Int3(Scene):
    def construct(self):
        title = Title("Cauchy's Theorem: visualized", color=BLUE_B)

        self.play(Write(title, run_time=1.5))

        self.wait(5)

        t1 = Tex(r"If $f(z)$ is analytic everywhere inside a simple loop $K$ bounding a region $R$, "
                 r"its Polya vector field in $R$ will have \textbf{zero flux density} and \textbf{zero work density}.",
                 color=PURPLE_C).shift(UP * 1)

        t1.scale(0.75)

        t2 = Tex(r"Intuitively, this means that there is no net flux of 'fluid' out of $R$, "
                 r"and that a puck fired round $K$ returns with its kinetic energy unchanged.",
                 color=GREEN_C)

        t2.next_to(t1, DOWN)

        t2.scale(0.75)

        self.play(Write(t1, run_time=2))

        self.wait(10)

        self.play(Write(t2, run_time=2))

        self.wait(12)
        
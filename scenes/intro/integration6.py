from manim import *


class Integration6(Scene):
    def construct(self):
        title = Title("Complex integration: a problem??", color=BLUE_B)

        self.play(Write(title, run_time=1.5))

        self.wait(4)

        t1 = Tex(r"Consider the integral $\int_{C} f(z) dz$:",
                 color=GREEN_C).shift(UP * 1.75)

        t1.scale(0.75)



        t2 = Tex(r"\begin{itemize}"
                 r"\item $f(z) = |f(z)|e^{i\beta}$, where $\beta$ is the angle $\mathbf{f}$ makes with the positive real axis at $z$."
                 r"\item $dz = e^{i\alpha}ds$, where $\alpha$ is the angle $\mathbf{dz}$ makes with the positive real axis and $ds$ is the differential length along $C$."
                 r"\end{itemize}",
                 color=PURPLE_A)

        t2.next_to(t1, DOWN)

        t2.scale(0.75)

        t3 = Tex(r"This integral can be expressed as $\int_{C} |f(z)|e^{i(\alpha+\beta)}\>ds$.",
                 color=RED_A)

        t3.scale(0.75)

        t3.next_to(t2, DOWN)

        self.play(Write(t1, run_time=2))

        self.wait(5)

        self.play(Write(t2, run_time=11))

        self.wait(5)
        self.play(Write(t3, run_time=2))

        self.wait(18)

        self.remove(t3)

        t4 = Tex(r"Integrating this term involves the addition of angles, which is not easy to visualize.",
                 color=GREEN_C).shift(UP * 1.75)

        t4.scale(0.75)

        self.play(Transform(t1, t4))

        t5 = Tex(r"It is often easier to consider the difference between two angles $\theta = \alpha - \beta$, "
                 r"as this angle is used to calculate helpful quantities, "
                 r"such as the work and flux of the curve, "
                 r"using the cosine and sine of this angle $\theta$, respectively.",
                 color=RED_A).shift(DOWN * 0.2)

        t5.scale(0.75)

        self.play(Transform(t2, t5))

        self.wait(22)








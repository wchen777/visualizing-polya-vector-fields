from manim import *


class Polya8(Scene):
    def construct(self):
        title = Title("Re-expressing our integrand", color=BLUE_B)

        self.play(Write(title, run_time=1.5))

        self.wait(5)

        t1 = Tex(r"First, define $\bar{f} = |\bar{f}|e^{-i\beta}$.",
                 color=YELLOW_B).shift(UP * 1.85)

        t1.scale(0.75)

        t2 = Tex(r"We can then define: "
                 r"\begin{align*} "
                 r"f dz &= \left(|f|e^{i\beta}\right)\left(e^{i\alpha}ds\right) \\ "
                 r"&= |f|e^{i(\alpha + \beta)}ds \\ "
                 r"&= |\bar{f}|e^{i(\alpha - (-\beta))}ds \\ "
                 r"&= |\bar{f}|e^{i\theta}ds "
                 r"\end{align*}",
                 color=MAROON_A)

        t2.next_to(t1, DOWN)

        t2.scale(0.75)

        t3 = Tex(r"where $\theta$ is the angle between $dz$ and $\bar{f}$.",
                 color=TEAL_E)

        t3.scale(0.75)

        t3.next_to(t2, DOWN)

        self.play(Write(t1, run_time=2))

        self.wait(5)

        self.play(Write(t2, run_time=11))

        self.play(Write(t3, run_time=2))

        self.wait(25)

        title2 = Title("Redefining our integral", color=BLUE_B)

        self.play(Transform(title, title2))

        t4 = Tex(r"Given that $ f dz = |\bar{f}|e^{i\theta}ds$, then",
                 color=GOLD_A).shift(UP * 1.85)

        t4.scale(0.75)

        self.play(Transform(t1, t4))

        t5 = Tex(r"\begin{align*} \int_{C} f(z) dz "
                 r"&= \int_{C} |\bar{f}|e^{i\theta}ds \\ "
                 r"&= \int_{C} |\bar{f}|\left[ \cos{\theta} + i\sin{\theta} \right]ds \\ "
                 r"&= \int_{C} \boldsymbol{\bar{f} \cdot T} ds + i\int_{C} \boldsymbol{\bar{f} \cdot N} ds "
                 r"\end{align*}",
                 color=MAROON_B)

        t5.scale(0.75)

        self.wait(5)

        self.play(Transform(t2, t5))

        t6 = Tex(r"Where $\boldsymbol{T}$ is a unit tangent vector in the direction of the path "
                 r"and $\boldsymbol{N}$ is unit normal vector in the direction of our path.", color=TEAL_D)

        t6.scale(0.75)

        t6.next_to(t5, DOWN)

        self.play(Transform(t3, t6))

        self.wait(25)

        t_title = Tex(r"Notice that the real and imaginary parts of each term in the integral "
                      r"are the \textbf{work and flux of the Pólya vector field for the "
                      r"corresponding element of the contour}!",
                 color=PURPLE_A).shift(UP * 0.8)

        t_title.scale(0.75)

        eq_new = Tex(r"$\int_{C} \boldsymbol{\bar{f} \cdot T} ds + i\int_{C} \boldsymbol{\bar{f} \cdot N} ds$", color=RED_A)
        eq_new.scale(0.75)
        eq_new.next_to(t_title, DOWN)

        self.remove(t6)
        self.remove(t3)
        # self.remove(t1)

        self.play(Transform(t1, t_title))

        # self.remove(t2)

        self.play(Transform(t2, eq_new))

        self.wait(12)

        t_title_2 = Tex(r"Our integral can now be expressed as:", color=GOLD_B).shift(UP * 0.75)

        t_title_2.scale(0.75)

        self.play(Transform(t1, t_title_2))

        eq_new_2 = Tex(r"$     \int_{C} f(z) dz = \text{Work}\left[ \boldsymbol{\overline{f}}, "
                       r"C \right] + i \cdot \text{Flux}\left[ \boldsymbol{\overline{f}}, C \right]$",
                     color=RED_B)
        eq_new_2.next_to(t_title_2, DOWN)

        eq_new_2.scale(0.75)

        self.play(Transform(t2, eq_new_2))

        self.wait(15)




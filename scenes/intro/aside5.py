from manim import *


class Aside5(Scene):
    def construct(self):
        title = Title("Aside: work and flux", color=BLUE_B)
        self.add(title)

        t1 = Tex(r"Suppose we have a complex function $f(z)$ with vector field $\mathbf{f}$, "
                 r"along with a curve $C$ in the complex plane.",
                 color=PURPLE_A).shift(UP * 2.0)

        t1.scale(0.75)

        t2 = Tex(r"The work of $\mathbf{f}$ along $C$ is the total magnitude of the field tangent to the curve, "
                 r"given by",
                 color=GOLD_B)

        t2.scale(0.75)

        eq3 = Tex(r"$\int_{C} \boldsymbol{\bar{f} \cdot T} ds$",
                 color=RED_B)

        eq3.next_to(t2, DOWN)

        t3 = Tex(r"Where $\boldsymbol{T}$ is a unit tangent vector in the direction of the curve and $ds$ "
                 r"is the instantaneous differential length of the curve.",
                 color=TEAL_D)

        t3.scale(0.75)

        t3.next_to(eq3, DOWN)

        self.play(Write(t1, run_time=2))

        self.wait(5)

        self.play(Write(t2, run_time=2))
        self.play(Write(eq3))
        self.play(Write(t3, run_time=3))
        self.wait(17)

        t4 = Tex(r"The flux of $\mathbf{f}$ along $C$ is the total magnitude of the field normal to the curve, "
                 r"given by",
                 color=GOLD_B)

        t4.scale(0.75)

        eq4 = Tex(r"$\int_{C} \boldsymbol{\bar{f} \cdot N} ds$",
                 color=RED_B)

        eq4.next_to(t4, DOWN)

        t5 = Tex(r"Where $\boldsymbol{N}$ is unit normal vector in the direction of our path and $ds$ "
                 r"is the instantaneous differential length of the curve.",
                 color=TEAL_D)

        t5.next_to(eq4, DOWN)

        t5.scale(0.75)

        self.play(Transform(t2, t4))
        self.play(Transform(eq3, eq4))
        self.play(Transform(t3, t5))

        self.wait(13)




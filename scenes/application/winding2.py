from manim import *


class Winding2(Scene):
    def construct(self):
        title = Title("Area as flux", color=BLUE_B)

        self.play(Write(title, run_time=1.5))

        self.wait(8)

        t1 = Tex(r"Recall the following result:",
                 color=TEAL_A).shift(UP * 1.75)

        t1.scale(0.75)

        t2 = Tex(r"$\oint_{C} \bar{z} dz = 2iA$",
                 color=GREEN_A)

        t2.next_to(t1, DOWN)

        t2.scale(0.75)

        t3 = Tex(r"We'd like to show this result using Polya vector fields, "
                 r"instead of Green's or Stokes's Theorem.",
                 color=RED_A).shift(DOWN* 0.5)

        t3.scale(0.75)

        self.play(Write(t1, run_time=2))

        self.wait(2)

        self.play(Write(t2, run_time=2))

        self.wait(5)

        self.play(Write(t3, run_time=2))

        self.wait(15)

        t4 = Tex(r"Let's start by rewriting our integral in terms of flux density and work density:",
                 color=GOLD_A).shift(UP * 1.65)

        t4.scale(0.75)

        self.play(Transform(t1, t4))

        t5 = Tex(r"\begin{align*} \oint_{C} \bar{z} dz "
                 r"&= \text{Work}\left[ \boldsymbol{z}, C \right] + i \cdot \text{Flux}\left[ \boldsymbol{z}, C \right] \\ "
                 r"&= \int\int_{R} \left[ \mathbf{\nabla} \times \mathbf{z} \right] dA +  "
                 r"i \cdot \int\int_{R} \left[ \mathbf{\nabla} \cdot \mathbf{z} \right] dA\\ "
                 r"\end{align*}",
                 color=MAROON_B)

        t5.scale(0.75)

        t5.next_to(t4, DOWN)

        self.wait(5)

        self.play(Transform(t2, t5))

        t6 = Tex(r"Where $R$ is the region bounded by the contour $C$.", color=TEAL_D)

        t6.scale(0.75)

        t6.next_to(t5, DOWN)

        self.play(Transform(t3, t6))

        self.wait(17)

        self.remove(t3)

        t5moved = Tex(r"\begin{align*} \oint_{C} \bar{z} dz "
                 r"&= \text{Work}\left[ \boldsymbol{z}, C \right] + i \cdot \text{Flux}\left[ \boldsymbol{z}, C \right] \\ "
                 r"&= \int\int_{R} \left[ \mathbf{\nabla} \times \mathbf{z} \right] dA +  "
                 r"i \cdot \int\int_{R} \left[ \mathbf{\nabla} \cdot \mathbf{z} \right] dA\\ "
                 r"\end{align*}",
                 color=MAROON_B).shift(DOWN * 1)
        t5moved.scale(0.75)

        self.play(Transform(t2, t5moved))

        t7 = Tex(r"$\mathbf{\nabla} \cdot \mathbf{z} = "
                 r"{\frac{\partial}{\partial x} \choose \frac{\partial}{\partial y}} \cdot {x \choose y} = 2$",
                 color=TEAL_D).shift(UP * 1.75)

        t7.scale(0.9)

        self.play(Transform(t1, t7))

        t8 = Tex(r"$\mathbf{\nabla} \times \mathbf{z} = "
                 r"{\frac{\partial}{\partial x} \choose \frac{\partial}{\partial y}} \times {x \choose y} = 0$",
                 color=BLUE_A)

        t8.scale(0.9)

        t8.next_to(t7, DOWN)

        self.play(Write(t8, run_time=1))

        self.wait(15)

        t9 = Tex(r"\begin{align*}"
                 r"\oint_{C} \bar{z} dz &= 0 + i \cdot \int\int_{R} 2 dA \\"
                 r"&= \boxed{2iA} \\"
                 r"\end{align*}", color=RED_C)

        t9.scale(0.9)

        t9.next_to(t8, DOWN)

        self.play(Transform(t2, t9))

        self.wait(20)


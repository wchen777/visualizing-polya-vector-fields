from manim import *


class Outro1(Scene):
    def construct(self):
        title = Title("What we've learned", color=BLUE_B)

        self.play(FadeIn(title))

        self.wait(4)

        t1 = Tex(r"- A visual basis to visualize complex functions through their Polya vector fields",
                 color=PURPLE_A).shift(UP * 2.0)

        t1.scale(0.70)

        t2 = Tex(r"- Showed how Polya vector fields help us visualize complex integration",
                 color=GOLD_B)

        t2.scale(0.70)

        t2.next_to(t1, DOWN)

        t3 = Tex(r"- Sourceless and irrotational property of Polya vector fields of analytic functions ",
                 color=RED_B)

        t3.next_to(t2, DOWN)

        t3.scale(0.7)

        t4 = Tex(r"- Cauchy’s Theorem in terms of Polya vector fields",
                 color=TEAL_D)

        t4.scale(0.70)

        t4.next_to(t3, DOWN)

        t5 = Tex(r"- Area as flux and winding numbers as flux",
                 color=YELLOW_B)

        t5.scale(0.70)

        t5.next_to(t4, DOWN)

        self.play(Write(t1, run_time=2))
        self.wait(6)

        self.play(Write(t2, run_time=2))
        self.wait(5)

        self.play(Write(t3, run_time=2))
        self.wait(6)

        self.play(Write(t4, run_time=1.5))
        self.wait(3.5)

        self.play(Write(t5, run_time=1.5))
        self.wait(3.5)




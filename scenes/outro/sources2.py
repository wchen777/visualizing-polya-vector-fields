from manim import *


class Sources2(Scene):
    def construct(self):
        title = Title("Thanks for watching!").set_color_by_gradient(BLUE_C, GREEN_C)

        self.play(FadeIn(title))

        t1 = Tex(r"\textbf{Sources}:",
                 color=RED_D).shift(UP * 1.75)

        t1.scale(0.9)

        t2 = Tex(r"\textit{Visual Complex Analysis} - Tristan Needham",
                 color=PURPLE_A).shift(UP * 1)

        t2.scale(0.8)


        t3 = Tex(r"- \text{Polya Plot and Polya Vector Fields} - Wolfram",
                 color=PURPLE_A)

        t3.next_to(t2, DOWN)

        t3.scale(0.8)

        t4 = Tex(r"- Manim Library - 3Blue1Brown",
                 color=PURPLE_A)

        t4.scale(0.8)

        t4.next_to(t3, DOWN)

        t5 = Tex(r"- The music of 3Blue1Brown - Vincent Rubinetti",
                 color=PURPLE_A)

        t5.scale(0.70)

        t5.next_to(t4, DOWN)

        self.play(Write(t1, run_time=2))
        self.wait(1.5)

        self.play(Write(t2, run_time=1))
        self.play(Write(t3, run_time=1))
        self.play(Write(t4, run_time=1))
        self.play(Write(t5, run_time=1))
        self.wait(8)




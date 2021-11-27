from manim import *


class Visualizing3(Scene):
    def construct(self):
        title = Title("The vector field interpretation", color=BLUE_B)
        self.add(title)

        t1 = Tex(r"Let's try and visualize a complex function $f(z)$ in a \textit{single} complex plane.",
                 color=GOLD_B).shift(UP * 2.0)

        t1.scale(0.75)

        t2 = Tex(r"The input value $z$ will be a point in our complex plane, but instead, "
                 r"\textit{the value of $f(z)$ is pictured as a vector emanating from $z$}.",
                 color=MAROON_B)

        t2.scale(0.75)

        t2.next_to(t1, DOWN)

        t3 = Tex(r"We now have a \textbf{vector field} of $f$!",
                 color=GREEN_B).shift(DOWN * 1)

        t3.scale(0.8)

        self.play(Write(t1, run_time=1.6))

        self.wait(1.5)

        self.play(Write(t2, run_time=3))
        self.wait(1.5)
        self.play(Write(t3))
        self.wait(3.5)




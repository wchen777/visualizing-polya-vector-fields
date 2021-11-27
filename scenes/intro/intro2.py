from manim import *


class Intro2(Scene):
    def construct(self):
        t1 = Tex(r"Our goal is to introduce a completely new way of visualizing complex functions, "
                    r"specifically focusing on how they can be used to \textbf{visualize complex integration}.",
                    color=PURPLE_B).shift(UP * 0.7)

        t1.scale(0.70)
        t2 = Tex(r" We hope to produce new insight into how to think about complex functions, "
                 r"and will end up finding that there are many surprising connections with physics!",
                 color=TEAL_B)

        t2.scale(0.70)

        t2.next_to(t1, DOWN)

        self.play(Write(t1, run_time=3))
        self.wait(8)
        self.play(Write(t2, run_time=3))
        self.wait(6)
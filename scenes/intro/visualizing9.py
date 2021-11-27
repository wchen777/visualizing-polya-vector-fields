from manim import *


class Visualizing9(Scene):
    def construct(self):
        title = Tex(r"Given this definition, we can examine a certain contour along a Pólya vector field "
                    r"and quickly get a feel for the value of the integral by "
                    r"\textbf{looking at how much the field flows \textit{along} "
                    r"and \textit{across} the contour}!!", color=PURPLE_C)

        title.scale(0.75)

        self.play(Write(title, run_time=3))
        self.wait(10)

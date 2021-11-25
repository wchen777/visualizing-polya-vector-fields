from manim import *
import math

class Intro1(GraphScene):

    def __init__(self):
        GraphScene.__init__(self,
                            x_min=-2,
                            x_max=2,
                            graph_origin=ORIGIN,
                            stroke_width=0.7,
                            axes_color=GOLD_A,
                            y_min=-2,
                            y_max=2,
                            y_axis_label="iy",
                            y_axis_height=3.5,
                            x_axis_width=3.5,
                            x_axis_label="x",
                            x_label_font_size=0.5,
                            y_label_font_size=0.5,
                            scale=0.5)

    def construct(self):
        first = Tex(r"Throughout our study of complex analysis, "
                    r"we've focused on one way of visualizing complex functions, "
                    r"namely as a \textbf{mapping of points in one complex plane to points in another}.", color=GOLD_B)

        first.to_corner(UP)
        first.scale(0.70)

        second = Tex(r"We used two planes, the \textbf{pre-image} and the \textbf{image}, "
                     r"to describe this mapping.", color=BLUE_B)

        second.scale(0.70)

        second.next_to(first, DOWN)

        self.play(Write(first, run_time=4))
        self.wait(9)
        self.play(Write(second, run_time=2))
        self.wait(6)

        self.graph_origin = 1.4 * DOWN + 4 * LEFT
        self.setup_axes(animate=True)

        # graph_left = self.get_graph(lambda x: PI / 4, y_min=-2, y_max=2, color=BLUE_A)

        graph_line = self.get_graph(lambda x: 2, y_min=-2, y_max=2, color=BLUE)

        graph_left = self.get_vertical_line_to_graph(1, graph_line, color=RED_B)
        self.play(Create(graph_left), run_time=1)

        # self.play(Create(ParametricFunction(lambda t: [0, t, 0], t_min=0, t_max=1)),
        #           run_time=1)

        self.wait(1.5)

        curvedArrow = CurvedArrow(start_point=np.array([-2, -1.5, 0]),
                                  end_point=np.array([2, -1.5, 0]), color=BLUE_B, angle=-PI/2)

        curvedArrow.scale(0.5)
        label = Tex(r"$e^z$", color=RED_B)
        label.scale(1.1)
        label.next_to(curvedArrow, UP)

        self.play(Create(curvedArrow))
        self.play(Write(label))

        self.wait(1.5)

        self.graph_origin = 1.4 * DOWN + 4 * RIGHT
        self.setup_axes(animate=True)

        # graph_right = self.get_graph(ParametricFunction(lambda t: [math.sin(t), math.cos(t), 0], ) color=RED_B)
        graph_right1 = self.get_graph(lambda x: math.sqrt(1 - x**2), x_min=-1, x_max=1, color=RED_B)
        graph_right2 = self.get_graph(lambda x: -math.sqrt(1 - x**2), x_min=1, x_max=-1, color=RED_B)

        # self.play(Create(ParametricFunction(lambda t: [math.sin(t), math.cos(t), 0], t_min=0, t_max=2*PI)),
        # run_time=1)
        self.play(Create(graph_right1), run_time=1)
        self.play(Create(graph_right2), run_time=1)



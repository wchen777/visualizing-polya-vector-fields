from manim import *
import math


def complex_exp(point):
    x, y = point[:2]
    result = Vector(np.array([math.exp(x) * math.cos(y), math.exp(x) * math.sin(y), 0]) - point, color=GOLD_D).shift(point)
    return result


def complex_exp_normal(point):
    x, y = point[:2]

    vec = np.array([math.exp(x) * math.cos(y), math.exp(x) * math.sin(y), 0]) - point
    vec = vec / (np.linalg.norm(vec) * 1.5)
    result = Vector(vec, color=GOLD_D).shift(point)
    return result


class VecField1(VectorScene):
    def __init__(self):
        VectorScene.__init__(self,
                             plane_kwargs={
                                 "color": RED
                             })

    def construct(self):
        func_tex = (
            Tex(r"$f(z) = e^z$")
                .to_edge(UL)
                .add_background_rectangle(BLACK)
        )

        plane = self.add_plane(animate=True).add_coordinates(x_values=[-5, 5], y_values=[-5, 5])

        plane.add(plane.get_axis_labels(y_label_tex="iy"))  # add x and y label
        self.add(plane)  # Place grid on screen
        self.add_foreground_mobject(func_tex)

        self.wait(3)

        vexample = self.add_vector(Vector(np.array([math.exp(1) - 1, 0]), color=GOLD_B).shift(np.array([1, 0, 0])))
        self.vector_to_coords(vector=vexample, integer_labels=False)

        self.wait(2)

        for x in range(-1, 2):
            for y in range(-1, 2):
                act_x = 0.5 * x
                act_y = 0.5 * y
                self.add_vector(complex_exp(np.array([act_x, act_y, 0])))

        self.wait(5)

        self.clear()

        plane = self.add_plane(animate=True).add_coordinates(x_values=[-5, 5], y_values=[-5, 5])

        plane.add(plane.get_axis_labels(y_label_tex="iy"))  # add x and y label
        self.add(plane)  # Place grid on screen
        self.add_foreground_mobject(func_tex)

        field = VGroup(*[complex_exp(x * RIGHT+y * UP)
                         for x in np.arange(-3, 3, 0.5)
                         for y in np.arange(-3, 3, 0.5)
                         ])

        self.play(Create(field))

        self.wait(12)

        self.clear()

        plane = self.add_plane().add_coordinates(x_values=[-5, 5], y_values=[-5, 5])

        plane.add(plane.get_axis_labels(y_label_tex="iy"))  # add x and y label
        self.add(plane)  # Place grid on screen
        self.add_foreground_mobject(func_tex)

        field = VGroup(*[complex_exp_normal(x * RIGHT + y * UP)
                         for x in np.arange(-5, 5, 0.5)
                         for y in np.arange(-5, 5, 0.5)
                         ])

        stuff = VGroup(plane, field, func_tex)

        self.play(Create(field))

        self.wait(15)

        box = RoundedRectangle(
            height=3, width=4, corner_radius=0.1, stroke_color=BLACK
        ).to_edge(DOWN)

        self.play(stuff.animate.move_to(box.get_center()).set(width=4), run_time=3)

        t1 = Tex(r"The original vector field representation remedies a shortcoming "
                 r"in the pre-image and image complex mapping.",
                 color=GOLD_B).shift(UP * 2.4)

        t1.scale(0.75)

        t2 = Tex(r"We are able to get a better feel for the overall behavior "
                 r"of a complex function as we inspect its vector field.",
                 color=MAROON_B)

        t2.scale(0.75)

        t2.next_to(t1, DOWN)

        t3 = Tex(r"However, there is one small caveat to the viability of this representation, "
                 r"which is where \textbf{Polya vector fields} come into play!",
                 color=TEAL_A)

        t3.scale(0.75)

        t3.next_to(t2, DOWN)

        self.play(Write(t1, run_time=2))

        self.wait(5)

        self.play(Write(t2, run_time=2))
        self.wait(5)
        self.play(Write(t3), run_time=2)
        self.wait(5)

#
#  def construct(self):
#
#         code = (
#             Code(
#                 "Tute3Vectors.py",
#                 style=Code.styles_list[12],
#                 background="window",
#                 language="python",
#                 insert_line_no=True,
#                 tab_width=2,
#                 line_spacing=0.3,
#                 scale_factor=0.5,
#                 font="Monospace",
#             )
#             .set_width(6)
#             .to_edge(UL, buff=0)
#         )
#
#         plane = self.add_plane(animate=True).add_coordinates()
#         self.play(Write(code), run_time=6)
#         self.wait()
#         vector = self.add_vector([-3, -2], color=YELLOW)
#
#         basis = self.get_basis_vectors()
#         self.add(basis)
#         self.vector_to_coords(vector=vector)
#
#         vector2 = self.add_vector([2, 2])
#         self.write_vector_coordinates(vector=vector2)

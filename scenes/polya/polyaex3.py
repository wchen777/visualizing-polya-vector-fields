from manim import *
import math

COLOR_ARRAY = ['#236B8E', YELLOW_B, GREEN_B, GOLD_B]


def get_color_from_mag(mag):
    if mag > 50:
        return RED_D
    elif mag > 25:
        return ORANGE
    elif mag > 7.5:
        return GOLD_D
    elif mag > 2.5:
        return YELLOW_B
    else:
        return GREEN_B


def get_div_factor_from_mag(mag):
    if mag > 50:
        return 1.5
    elif mag > 25:
        return 1.65
    elif mag > 10:
        return 1.85
    elif mag > 5:
        return 2.2
    else:
        return 2.75


def complex_sin_conj_streamlines(point):
    x, y = point[:2]
    return 1.5 * ((math.sin(x) * math.cosh(y) * RIGHT) + (-1 * math.cos(x) * math.sinh(y) * UP))


def complex_sin_conj_normal(point):
    x, y = point[:2]

    vec = np.array([math.sin(x) * math.cosh(y),
                    -1 * math.cos(x) * math.sinh(y), 0])

    mag = np.linalg.norm(vec)

    if mag == 0:
        return Vector(np.array([0, 0, 0]), color=GREEN_B).shift(point)

    color = get_color_from_mag(mag)

    div_factor = get_div_factor_from_mag(mag)

    vec = vec / (mag * div_factor)

    result = Vector(vec, color=color).shift(point)
    return result


def curve1(t):
    return [math.cos(t), math.sin(t), 0]


class ExPolya3(VectorScene):
    def __init__(self):
        VectorScene.__init__(self,
                             plane_kwargs={
                                 "color": RED
                             })

    def construct(self):
        func_tex = (
            Tex(r"$f(z) = \sin(z)$")
                .to_edge(UL)
                .add_background_rectangle(BLACK)
        )

        field_tex = (Tex(r"$\mathbf{f} = (\sin{x}\cosh{y}, -\cos{x}\sinh{y})$")
                     .to_edge(UR)
                     .shift(DOWN*0.25)
                     .add_background_rectangle(BLACK))

        plane = self.add_plane(animate=True).add_coordinates(x_values=[-7, 7], y_values=[-7, 7])

        plane.add(plane.get_axis_labels(y_label_tex="iy"))  # add x and y label
        self.add(plane)  # Place grid on screen
        self.add_foreground_mobject(func_tex)
        self.add_foreground_mobject(field_tex)

        field = VGroup(*[complex_sin_conj_normal(x * RIGHT + y * UP)
                         for x in np.arange(-7, 7, 0.5)
                         for y in np.arange(-7, 7, 0.5)
                         ])

        self.play(Create(field, run_time=3))

        self.wait(5)

        paracurve = ParametricFunction(curve1, t_range=[-PI / 2, 3 * PI / 2], color=PURPLE_A, stroke_width=6)
        self.play(Create(paracurve))

        self.wait(1)

        stream_lines_exp = StreamLines(complex_sin_conj_streamlines,
                                       x_range=[-7, 7, 0.3], y_range=[-7, 7, 0.3],
                                       colors=COLOR_ARRAY,
                                       padding=1, stroke_width=2)

        self.add(stream_lines_exp)

        stream_lines_exp.start_animation(warm_up=False, flow_speed=1.5)

        self.wait(8)


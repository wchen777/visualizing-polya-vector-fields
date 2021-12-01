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


def get_color_from_mag_new(mag):
    if mag > 6:
        return RED_D
    elif mag > 4:
        return ORANGE
    elif mag > 1.5:
        return GOLD_D
    elif mag > 0.85:
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


def z_normal(point):
    x, y = point[:2]

    vec = np.array([x, y, 0])

    mag = np.linalg.norm(vec)

    if mag == 0:
        return Vector(np.array([0, 0, 0]), color=GREEN_B).shift(point)

    color = get_color_from_mag(mag)

    div_factor = get_div_factor_from_mag(mag)

    vec = vec / (mag * div_factor)

    result = Vector(vec, color=color).shift(point)
    return result


def z_normal_new(point):
    x, y = point[:2]

    vec = np.array([x, y, 0])

    mag = np.linalg.norm(vec)

    if mag == 0:
        return Vector(np.array([0, 0, 0]), color=GREEN_B).shift(point)

    color = get_color_from_mag_new(mag)

    div_factor = get_div_factor_from_mag(mag)

    vec = vec / (mag * div_factor)

    result = Vector(vec, color=color).shift(point)
    return result


def z_conj_streamlines(point):
    x, y = point[:2]
    return 1.5 * ((x * RIGHT) + (y * UP))


def curve1arc(t):
    return [math.cos(t), math.sin(t), 0]


def curveline1(t):
    return [0, t, 0]


def curveline2(t):
    return [-t, 0, 0]


def curveline3(t):
    return [t, 0, 0]


def curve2arc(t):
    return [3 * math.cos(-t + PI / 2), 3 * math.sin(-t + PI / 2), 0]


class WindingEx3(VectorScene):
    def __init__(self):
        VectorScene.__init__(self)

    def construct(self):
        func_tex = (
            Tex(r"$f(z) = \bar{z}$")
                .to_edge(UL)
                .add_background_rectangle(BLACK, opacity=1)
        )

        field_tex = (Tex(r"$\mathbf{f} = (x, y)$")
                     .to_edge(UR)
                     .shift(DOWN * 0.25)
                     .add_background_rectangle(BLACK, opacity=1))

        plane = self.add_plane(animate=True).add_coordinates(x_values=[-7, 7], y_values=[-7, 7])

        plane.add(plane.get_axis_labels(y_label_tex="iy"))  # add x and y label
        self.add(plane)  # Place grid on screen
        self.add_foreground_mobject(func_tex)
        self.add_foreground_mobject(field_tex)

        field = VGroup(*[z_normal(x * RIGHT + y * UP)
                         for x in np.arange(-7, 7, 1 / 3)
                         for y in np.arange(-7, 7, 1 / 3)
                         ])

        self.play(Create(field, run_time=3))

        field_new = VGroup(*[z_normal_new(x * RIGHT + y * UP)
                             for x in np.arange(-7, 7, 1 / 3)
                             for y in np.arange(-7, 7, 1 / 3)
                             ])

        self.wait(4)

        self.play(Transform(field, field_new, run_time=2.5))

        # stream_lines_zb = StreamLines(z_conj_streamlines,
        #                                x_range=[-7, 7, 0.3], y_range=[-7, 7, 0.3],
        #                                colors=COLOR_ARRAY,
        #                                padding=1, stroke_width=2)
        #
        # self.add(stream_lines_zb)
        #
        # stream_lines_zb.start_animation(warm_up=False, flow_speed=1.5)

        self.wait(1)

        theta_1 = 0
        theta_2 = PI / 2

        paracurvearc = ParametricFunction(curve1arc, t_range=[theta_1, theta_2], color=PINK, stroke_width=6)
        self.play(Create(paracurvearc, run_time=1))

        paracurveline1 = ParametricFunction(curveline1, t_range=[1, 3], color=PINK, stroke_width=6)
        self.play(Create(paracurveline1, run_time=1))

        paracurve2arc = ParametricFunction(curve2arc, t_range=[theta_1, theta_2], color=PINK, stroke_width=6)
        self.play(Create(paracurve2arc, run_time=1))

        paracurveline2 = ParametricFunction(curveline2, t_range=[-3, -1], color=PINK, stroke_width=6)
        self.play(Create(paracurveline2, run_time=1))

        self.wait(6)

        rad_label_1 = ParametricFunction(curveline3, t_range=[0, 1], color=RED_A, stroke_width=6)
        self.play(Create(rad_label_1, run_time=1))

        label_1_tex = (
            Tex(r"$b$")
                .next_to(rad_label_1, DOWN)
                .scale(0.7)
                .add_background_rectangle(BLACK, opacity=1)
        )

        self.play(Create(label_1_tex))

        rad_label_2 = ParametricFunction(curveline1, t_range=[0, 3], color=TEAL_A, stroke_width=6)
        self.play(Create(rad_label_2, run_time=1))

        label_2_tex = (
            Tex(r"$a$")
                .next_to(rad_label_2, LEFT)
                .scale(0.9)
                .add_background_rectangle(BLACK, opacity=1)
        )

        self.play(Create(label_2_tex))

        self.wait(10)

        self.remove(rad_label_1)
        self.remove(rad_label_2)

        label = Tex(r"$\phi$", color=BLUE_A).add_background_rectangle(BLACK).scale(0.9)

        label.move_to(0.1 * UP + 0.1 * RIGHT)

        self.play(Create(label))

        self.wait(10)

        # no flux on lines

        paracurveline1Trans = ParametricFunction(curveline1, t_range=[1, 3], color=YELLOW_C, stroke_width=6)
        paracurveline2Trans = ParametricFunction(curveline2, t_range=[-3, -1], color=YELLOW_C, stroke_width=6)

        paracurveline1Revert = ParametricFunction(curveline1, t_range=[1, 3], color=PINK, stroke_width=6)
        paracurveline2Revert = ParametricFunction(curveline2, t_range=[-3, -1], color=PINK, stroke_width=6)

        self.play(Transform(paracurveline1, paracurveline1Trans))
        self.play(Transform(paracurveline2, paracurveline2Trans))

        self.wait(10)

        self.play(Transform(paracurveline1, paracurveline1Revert))
        self.play(Transform(paracurveline2, paracurveline2Revert))

        # self.play(Transform(paracurveline2Trans, paracurveline2))
        # # self.play(Transform(paracurveline2, paracurveline2))
        # # self.play(Transform(paracurveline1, paracurveline1))
        # self.play(Transform(paracurveline1Trans, paracurveline1))

        self.wait(1)

        paracurvearcTrans = ParametricFunction(curve1arc, t_range=[theta_1, theta_2], color=YELLOW_C, stroke_width=6)
        paracurve2arcTrans = ParametricFunction(curve2arc, t_range=[theta_1, theta_2], color=YELLOW_C, stroke_width=6)

        paracurvearcRevert = ParametricFunction(curve1arc, t_range=[theta_1, theta_2], color=PINK, stroke_width=6)
        paracurve2arcRevert = ParametricFunction(curve2arc, t_range=[theta_1, theta_2], color=PINK, stroke_width=6)

        self.play(Transform(paracurve2arc, paracurve2arcTrans))
        self.play(Transform(paracurvearc, paracurvearcTrans))

        self.wait(16)

        self.play(Transform(paracurve2arc, paracurve2arcRevert))
        self.play(Transform(paracurvearc, paracurvearcRevert))

        # self.play(Transform(paracurve2arcTrans, paracurve2arc))
        # self.play(Transform(paracurve2arc, paracurve2arc))
        # self.play(Transform(paracurvearc, paracurvearc))
        # self.play(Transform(paracurvearcTrans, paracurvearc))

        self.wait(10)

        self.remove(field)
        self.remove(field_new)

        all = VGroup(plane,
                     func_tex, label, label_1_tex, label_2_tex,
                     field_tex, paracurve2arc, paracurvearc,
                     paracurveline1, paracurveline2
                     )

        box = RoundedRectangle(
            height=4, width=5, corner_radius=0.1, stroke_color=BLACK
        ).to_edge(DOWN)

        self.play(all.animate.move_to(box.get_center()).set(width=5, height=4), run_time=3)

        self.wait(3)

        t1 = Tex(r"The larger arc has length $a\phi$ and the speed of the 'fluid', or vectors, crossing it is $a$. "
                 r"Therefore, the flux across this arc is $a^2\phi$.", color=GOLD_B)

        t1.to_corner(UP)
        t1.scale(0.75)

        t2 = Tex(r"Similarly, the flux of the smaller arc is $b^2\phi$.", color=RED_B)
        t2.scale(0.75)

        t2.next_to(t1, DOWN)

        self.play(Write(t1, run_time=2))
        self.play(Write(t2))

        self.wait(12)

        t3 = Tex(r"Flux $=$ ('fluid' out) $-$ ('fluid' in) "
                 r"$= 2 \left[ \frac{1}{2}a^2\phi - \frac{1}{2}b^2\phi \right] =$ 2(Area of region).", color=TEAL_C)
        t3.next_to(t2, DOWN)

        t3.scale(0.75)
        self.play(Write(t3, run_time=2))

        self.wait(15)

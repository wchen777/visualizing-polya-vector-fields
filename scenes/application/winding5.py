from manim import *
import math

COLOR_ARRAY = ['#236B8E', YELLOW_B, GREEN_B, GOLD_B]


pts = [[0, -2.5, 0], [1, -2.7, 0], [2, -2.8, 0], [3, -2.7, 0], [4, -2.5, 0], [4.5, -1.5, 0], [4, -0.8, 0],
       [3.2, 0.3, 0], [2.5, -1.5, 0], [-0.1, 0.5, 0]]

pts_2 = [[-3, -0.5, 0], [-2, -0.7, 0], [-1, -0.8, 0], [0, -0.7, 0], [1, -0.5, 0], [1.5, 0.5, 0], [1, 1.2, 0],
         [0.2, 2.3, 0], [-1.5, 0.5, 0], [-2.9, 2.5, 0]]

winding_pts = [

    [0, 3, 0], [-0.4, 2.7, 0], [-1, 2.2, 0], [-1.8, 0.3, 0], [-1.3, -1.4, 0], [-1, -1.2, 0],
    [1.8, 1.2, 0], [2.3, 3.1, 0], [0, 3.7, 0], [-2.4, 3.4, 0], [-2.8, 2.9, 0], [-2.4, 3.1, 0], [-1.5, 3.25, 0],
    [-2.4, 2.5, 0], [-2.7, -1.3, 0], [0, -2, 0], [2.9, 0, 0], [0, 3, 0]
]


def apply_pts_transform(pts_arr):
    new_pts = []
    for pt in pts_arr:
        new_pt = pt
        new_pt[0] = new_pt[0] - 2.5
        new_pt[1] = new_pt[0] + 2
        print(len(new_pt))
        new_pts.append(new_pt)
    print(len(new_pts))
    return new_pts


def apply_pts_transform_winding(pts_arr):
    new_pts = []
    for pt in pts_arr:
        new_pt = pt
        new_pt[0] = 2.6 * new_pt[0] - 3
        new_pt[1] = 1.2 * new_pt[0] + 2
        new_pts.append(new_pt)

    return new_pts


def get_color_from_mag_new(mag):
    if mag > 2:
        return RED_D
    elif mag > 1:
        return ORANGE
    elif mag > 0.5:
        return GOLD_D
    elif mag > 0.25:
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


def over_z_normal(point):
    x, y = point[:2]

    if x == 0 and y == 0:
        return Vector(np.array([0, 0, 0]), color=GREEN_B).shift(point)

    vec = np.array([(x / (x**2 + y**2)), (y / (x**2 + y**2)), 0])

    mag = np.linalg.norm(vec)

    if mag == 0:
        return Vector(np.array([0, 0, 0]), color=GREEN_B).shift(point)

    color = get_color_from_mag_new(mag)

    div_factor = get_div_factor_from_mag(mag)

    vec = vec / (mag * div_factor)

    result = Vector(vec, color=color).shift(point)
    return result


def over_z_streamlines(point):
    x, y = point[:2]
    return 1.5 * (((x / (x ** 2 + y ** 2)) * RIGHT) + ((y / (x ** 2 + y ** 2)) * UP))


class WindingEx5(VectorScene):
    def __init__(self):
        VectorScene.__init__(self)

    def construct(self):
        func_tex = (
            Tex(r"$f(z) = \frac{1}{z}$")
                .to_edge(UL)
                .add_background_rectangle(BLACK, opacity=1)
        )

        field_tex = (Tex(r"$\mathbf{f} = (\frac{x}{x^2 + y^2}, \frac{y}{x^2 + y^2})$")
                     .to_edge(UR)
                     .shift(DOWN * 0.25)
                     .add_background_rectangle(BLACK, opacity=1))

        plane = self.add_plane(animate=True).add_coordinates(x_values=[-7, 7], y_values=[-7, 7])

        plane.add(plane.get_axis_labels(y_label_tex="iy"))  # add x and y label
        self.add(plane)  # Place grid on screen
        self.add_foreground_mobject(func_tex)
        self.add_foreground_mobject(field_tex)

        field = VGroup(*[over_z_normal(x * RIGHT + y * UP)
                         for x in np.arange(-7, 7, 0.5)
                         for y in np.arange(-7, 7, 0.5)
                         ])
        self.play(Create(field, run_time=3))

        self.wait(19)

        strength_tex = (Tex(r"'source of strength of $2 \pi$'")
                           .shift(LEFT * 1.5 + DOWN * 1.5)
                           .scale(0.8)
                           .add_background_rectangle(BLACK, opacity=1))

        self.play(FadeIn(strength_tex))
        self.wait(10)
        self.play(FadeOut(strength_tex))
        self.wait(17)

        rounded_1 = Polygon(*pts, stroke_color=LIGHT_PINK).round_corners(radius=0.6)

        self.play(FadeIn(rounded_1))

        self.wait(13)

        rounded_2 = Polygon(*pts_2, stroke_color=LIGHT_PINK).round_corners(radius=0.6)

        self.play(Transform(rounded_1, rounded_2))

        self.wait(15)

        integral_tex = (Tex(r"$\oint_{L} \frac{1}{z} dz ="
                            r" i \cdot \text{Flux}\left[ \frac{1}{\boldsymbol{\overline{z}}}, L \right]$")
                        .shift(LEFT * 1.5 + DOWN * 1.5)
                        .scale(0.7)
                        .add_background_rectangle(BLACK, opacity=1))

        integral_tex_2 = (Tex(r"$\oint_{L} \frac{1}{z} dz ="
                            r" 2\pi i \cdot $ (winding number of $L$ around the origin)")
                        .shift(LEFT * 1.5 + DOWN * 1.5)
                        .scale(0.7)
                        .add_background_rectangle(BLACK, opacity=1))

        self.play(FadeIn(integral_tex))
        self.wait(7)
        self.play(Transform(integral_tex, integral_tex_2))
        self.wait(7)
        self.play(FadeOut(integral_tex))

        self.wait(10)
        stream_lines = StreamLines(over_z_streamlines,
                                       x_range=[-7, 7, 0.2], y_range=[-7, 7, 0.2],
                                       colors=COLOR_ARRAY,
                                       padding=1, stroke_width=2)

        self.add(stream_lines)

        stream_lines.start_animation(warm_up=False, flow_speed=1.5)

        self.wait(12)

        self.play(FadeOut(stream_lines))

        self.wait(20)

        self.play(FadeOut(rounded_1))

        rounded_3 = Polygon(*winding_pts, stroke_color=BLUE_B).round_corners(radius=0.8)

        self.play(Transform(rounded_1, rounded_3))

        self.wait(10)

from manim import *


class Int1(Scene):
    def construct(self):
        title = Title("Polya vector fields of analytic functions: Theorem", color=BLUE_B)

        self.play(Write(title, run_time=1.5))

        self.wait(2)

        t1 = Tex(r"\textbf{Theorem: } \textit{Let $f(z)$ be a complex mapping. "
                 r"Then the Pólya vector field of $f(z)$ is divergence-less (sourceless) and "
                 r"curl-less (irrotational) if and only if $f(z)$ is an analytic function.}",
                 color=TEAL_B).shift(UP * 0.5)

        t1.scale(0.75)

        self.play(Write(t1, run_time=3))

        self.wait(10)

        self.remove(t1)

        title_proof = Title("Polya vector fields of analytic functions: Proof", color=BLUE_B)

        self.play(Transform(title, title_proof))

        div = Tex(r"The divergence of $\bar{\mathbf{f}}(z)$ is "
                  r"\begin{align*} \mathbf{\nabla} \cdot \bar{\mathbf{f}}(z) "
                  r"&= {\frac{\partial}{\partial x} \choose \frac{\partial}{\partial y}} \cdot {u(x,y)\choose -v(x,y)} \\ "
                  r"&= \frac{\partial u}{\partial x} - \frac{\partial v}{\partial y} \end{align*}",
                  color=PURPLE_B).shift(UP * 1.25)

        div.scale(0.7)

        curl = Tex(r"while its curl is "
                   r"\begin{align*} \mathbf{\nabla} \times \bar{\mathbf{f}}(z) "
                   r"&= {\frac{\partial}{\partial x} \choose \frac{\partial}{\partial y}} \times {u(x,y)\choose -v(x,y)} \\ "
                   r"&= -\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} \end{align*}", color=RED_B)

        curl.scale(0.7)

        curl.next_to(div, DOWN)

        self.play(Write(div, run_time=4))

        self.wait(2)

        self.play(Write(curl, run_time=4))

        self.wait(8)

        div_new = Tex(r"$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$",
                  color=PURPLE_B).shift(UP * 1.4)

        div_new.scale(1.2)

        curl_new = Tex(r"$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$", color=RED_B)

        curl_new.scale(1.2)

        curl_new.next_to(div_new, DOWN)

        self.play(Transform(div, div_new))

        self.wait(2)

        self.play(Transform(curl, curl_new))

        self.wait(5)

        holo = Tex("These are exactly the Cauchy-Riemann equations, "
                   "which are satisfied when $f(z)$ is analytic!", color=GOLD_B)

        holo.scale(0.75)

        holo.next_to(curl_new, DOWN * 1.3)

        self.play(Write(holo, run_time=2))

        self.wait(10)


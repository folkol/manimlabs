from manim import *
from manim.animation.transform import ApplyMethod

print(config)


class MyScene(Scene):
    def construct(self):
        g = PGroup()
        for sf in range(9):
            p = PointCloudDot(density=20, radius=1).thin_out(2 + sf)
            g.add(p)
        g.arrange_in_grid()
        self.add(g)
        animations = [Rotate(dot, angle=4 * PI, run_time=2, rate_func=rate_functions.ease_in_out_cubic)
                      for dot in g]
        animation_group = LaggedStart(*animations, lag_ratio=0.1)
        self.play(animation_group)

        self.next_section("Falling")

        all_points = []
        for dot in g:
            for point_coords in dot.points:
                point = Point(location=point_coords, color=dot.color, stroke_width=2)
                all_points.append(point)
                self.add(point)
            self.remove(dot)

        fall_distance = config.frame_height
        fall_animations = [ApplyMethod(point.shift, DOWN * fall_distance,
                                       run_time=np.random.uniform(0.5, 1.5),
                                       rate_func=rate_functions.ease_in_expo)
                           for point in all_points]
        fall_group = LaggedStart(*fall_animations, lag_ratio=0.0001)
        self.play(fall_group)

import unittest, math
from Shapes import Circle, Triangle


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), math.pi * 9)


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_triangle_is_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())

    def test_triangle_not_right(self):
        triangle = Triangle(2, 3, 4)
        self.assertFalse(triangle.is_right_angle())


if __name__ == "__main__":
    unittest.main()

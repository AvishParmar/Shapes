# Avish Parmar 112647892
from unittest import TestCase
import unittest
import rectangle


class TestRectangle(TestCase):

    def test_center(self):
        # Center in first quadrant
        r = rectangle.Rectangle(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)
        result = r.center()
        expected = rectangle.TwoDPoint(0.5, 0.5)
        self.assertEqual(expected, result)

        # Center in second quadrant
        r = rectangle.Rectangle(0.0, 1.0, -1.0, 1.0, -1.0, 0.0, 0.0, 0.0)
        result = r.center()
        expected = rectangle.TwoDPoint(-0.5, 0.5)

        # Center in third quadrant
        r = rectangle.Rectangle(0.0, 0.0, -1.0, 0.0, -1.0, -1.0, 0.0, -1.0)
        result = r.center()
        expected = rectangle.TwoDPoint(-0.5, -0.5)
        self.assertEqual(expected, result)

        # Center in fourth quadrant
        r = rectangle.Rectangle(1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0, -1.0)
        result = r.center()
        expected = rectangle.TwoDPoint(0.5, -0.5)
        self.assertEqual(expected, result)

        # Invalid rectangle:
        with self.assertRaises(TypeError) as cm:
            rectangle.Rectangle(-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0, -8.0)

    def test_area(self):
        # Area of rectangle that is also a square
        r = rectangle.Rectangle(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)
        result = r.area()
        expected = 1.0
        self.assertEqual(expected, result)

        # Area of a rectangle
        r = rectangle.Rectangle(20.0, 40.0, 5.0, 40.0, 5.0, 5.0, 20.0, 5.0)
        result = r.area()
        expected = 525
        self.assertEqual(expected, result)

        # Area of a rectangle with reversed coordinates
        r = rectangle.Rectangle(20.0, 5.0, 5.0, 5.0, 5.0, 40.0, 20.0, 40.0)
        result = r.area()
        expected = 525
        self.assertEqual(expected, result)

        # Invalid rectangle:
        with self.assertRaises(TypeError) as cm:
            rectangle.Rectangle(-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0, -8.0)

    def test_eq(self):
        # Check Equality
        r1 = rectangle.Rectangle(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)
        r2 = rectangle.Rectangle(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)
        result = r1.__eq__(r2)
        expected = True
        self.assertEqual(expected, result)

        # Check Inequality
        r1 = rectangle.Rectangle(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)
        r2 = rectangle.Rectangle(2.0, 2.0, 0.0, 2.0, 0.0, 0.0, 2.0, 0.0)
        result = r1.__eq__(r2)
        expected = False
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

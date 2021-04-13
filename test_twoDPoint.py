# Avish Parmar 112647892
from unittest import TestCase
import unittest
import two_d_point


class TestTwoDPoint(TestCase):

    def test_from_coordinates(self):
        # Check if it works properly for valid input
        result = two_d_point.TwoDPoint.from_coordinates([1.0, 2.0])
        expected = [two_d_point.TwoDPoint(1.0, 2.0)]
        self.assertEqual(expected, result)

        # Check for exception thrown for input thrown with 3 arguments
        self.assertRaises(Exception, two_d_point.TwoDPoint.from_coordinates, [1.0, 2.0, 3.0])

        # Check for exception thrown for input thrown with 1 argument
        self.assertRaises(Exception, two_d_point.TwoDPoint.from_coordinates, [1.0])

    def test_eq(self):
        # Check Equality
        p1 = two_d_point.TwoDPoint(1.0, 1.0)
        p2 = two_d_point.TwoDPoint(1.0, 1.0)
        result = p1.__eq__(p2)
        expected = True
        self.assertEqual(expected, result)

        # Check Inequality
        p1 = two_d_point.TwoDPoint(1.0, 1.0)
        p2 = two_d_point.TwoDPoint(1.5, 1.5)
        result = p1.__eq__(p2)
        expected = False
        self.assertEqual(expected, result)

    def test_add(self):
        # Test #1:
        p1 = two_d_point.TwoDPoint(1.0, 1.0)
        p2 = two_d_point.TwoDPoint(1.0, 1.0)
        result = p1.__add__(p2)
        expected = two_d_point.TwoDPoint(2.0, 2.0)
        self.assertEqual(expected, result)

        # Test #2:
        p1 = two_d_point.TwoDPoint(1.5, 1.5)
        p2 = two_d_point.TwoDPoint(1.5, 1.5)
        result = p1.__add__(p2)
        expected = two_d_point.TwoDPoint(3.0, 3.0)
        self.assertEqual(expected, result)

    def test_sub(self):
        # Test #1:
        p1 = two_d_point.TwoDPoint(1.0, 1.0)
        p2 = two_d_point.TwoDPoint(1.0, 1.0)
        result = p1.__sub__(p2)
        expected = two_d_point.TwoDPoint(0.0, 0.0)
        self.assertEqual(expected, result)

        # Test #2:
        p1 = two_d_point.TwoDPoint(5.0, 13.0)
        p2 = two_d_point.TwoDPoint(1.0, 1.0)
        result = p1.__sub__(p2)
        expected = two_d_point.TwoDPoint(4.0, 12.0)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

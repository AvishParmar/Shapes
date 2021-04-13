# Avish Parmar 112647892
from unittest import TestCase
import unittest
import square


class TestSquare(TestCase):

    def test_snap(self):
        # Valid Square with successful snap() round down execution
        s = square.Square(3.45, 3.45, 1.45, 3.45, 1.45, 1.45, 3.45, 1.45)
        result = s.snap()
        expected = square.Quadrilateral(3.0, 3.0, 1.0, 3.0, 1.0, 1.0, 3.0, 1.0)
        self.assertEqual(expected, result)

        # Valid Square with successful snap() round up execution
        s = square.Square(3.5, 3.5, 1.5, 3.5, 1.5, 1.5, 3.5, 1.5)
        result = s.snap()
        expected = square.Quadrilateral(4.0, 4.0, 2.0, 4.0, 2.0, 2.0, 4.0, 2.0)
        self.assertEqual(expected, result)

        # Valid Square with coordinates that have special conditions during rounding
        s = square.Square(0.5, 0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5)
        result = s.snap()
        expected = square.Quadrilateral(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)
        self.assertEqual(expected, result)

        # Valid Square with unsuccessful snap() execution
        with self.assertRaises(ValueError) as cm:
            square.Square(0.4, 0.4, 0.0, 0.4, 0.0, 0.0, 0.4, 0.0).snap()
        # Invalid Square

        with self.assertRaises(TypeError) as cm:
            square.Square(0.1, 0.4, 0.0, 0.4, 0.0, 0.0, 0.4, 0.0).snap()

    def test_eq(self):
        # Check Equality
        s1 = square.Square(3.0, 3.0, 0.0, 3.0, 0.0, 0.0, 3.0, 0.0)
        s2 = square.Square(3.0, 3.0, 0.0, 3.0, 0.0, 0.0, 3.0, 0.0)
        result = s1.__eq__(s2)
        expected = True
        self.assertEqual(expected, result)

        # Check Inequality
        s1 = square.Square(3.0, 3.0, 0.0, 3.0, 0.0, 0.0, 3.0, 0.0)
        s2 = square.Square(4.0, 4.0, 0.0, 4.0, 0.0, 0.0, 4.0, 0.0)
        result = s1.__eq__(s2)
        expected = False
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

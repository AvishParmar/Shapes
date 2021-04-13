# Avish Parmar 112647892
from unittest import TestCase
import unittest
import quadrilateral


class TestQuadrilateral(TestCase):

    # Test side lengths
    def test_side_lengths(self):
        # Test side lengths of Quadrilateral that is a Square
        result = quadrilateral.Quadrilateral(3.0, 3.0, 1.0, 3.0, 1.0, 1.0, 3.0, 1.0)
        side_lengths = result.side_lengths()
        expected = 2.0, 2.0, 2.0, 2.0
        self.assertEqual(expected, side_lengths)

        # Test side lengths of Quadrilateral that is a rectangle
        result = quadrilateral.Quadrilateral(4.0, 3.0, 1.0, 3.0, 1.0, 1.0, 4.0, 1.0)
        side_lengths = result.side_lengths()
        expected = 3.0, 2.0, 3.0, 2.0
        self.assertEqual(expected, side_lengths)

        # Test side lengths of Quadrilateral that is an arbitrary shape
        result = quadrilateral.Quadrilateral(4.0, 3.0, 2.0, 2.5, 1.0, 1.0, 3.0, 1.5)
        side_lengths = result.side_lengths()
        expected = 2.06155, 1.80278, 2.06155, 1.80278
        self.assertEqual(expected, side_lengths)

        # Test side lengths of Quadrilateral that spans over four quadrants
        result = quadrilateral.Quadrilateral(1.0, 1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0)
        side_lengths = result.side_lengths()
        expected = 2.0, 2.0, 2.0, 2.0
        self.assertEqual(expected, side_lengths)

        # Invalid Quadrilateral
        with self.assertRaises(TypeError) as cm:
            quadrilateral.Quadrilateral(-1.0, -2.0, -3.0, -4.0)

    def test_smallest_x(self):
        # Test smallest_x of Quadrilateral with the lowest x being 0.0, (vertex 2: (0.0, 0.0))
        result = quadrilateral.Quadrilateral(3.0, 3.0, 0.0, 3.0, 0.0, 0.0, 3.0, 0.0)
        smallest_x = result.smallest_x()
        expected = 0.0
        self.assertEqual(expected, smallest_x)

        # Test smallest x of Quadrilateral that spans over four quadrants
        result = quadrilateral.Quadrilateral(1.0, 1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0)
        smallest_x = result.smallest_x()
        expected = -1.0
        self.assertEqual(expected, smallest_x)

        # Test smallest x of Quadrilateral which only resides in the first quadrant
        result = quadrilateral.Quadrilateral(3.0, 3.0, 1.0, 3.0, 1.0, 1.0, 3.0, 1.0)
        smallest_x = result.smallest_x()
        expected = 1.0
        self.assertEqual(expected, smallest_x)

        # Invalid Quadrilateral
        with self.assertRaises(TypeError) as cm:
            quadrilateral.Quadrilateral(-1.0, -2.0, -3.0, -4.0)

    def test_eq(self):
        # Check Equality
        q1 = quadrilateral.Quadrilateral(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)
        q2 = quadrilateral.Quadrilateral(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)
        result = q1.__eq__(q2)
        expected = True
        self.assertEqual(expected, result)

        # Check Inequality
        q1 = quadrilateral.Quadrilateral(1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0)
        q2 = quadrilateral.Quadrilateral(2.0, 2.0, 0.0, 2.0, 0.0, 0.0, 2.0, 0.0)
        result = q1.__eq__(q2)
        expected = False
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

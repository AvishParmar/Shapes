# Avish Parmar 112647892
from math import sqrt

from two_d_point import TwoDPoint


class Quadrilateral:

    def __init__(self, *floats):
        points = TwoDPoint.from_coordinates(list(floats))
        self.__vertices = tuple(points[0:4])
        if not self.__is_member():
            raise TypeError("A Quadrilateral cannot be formed from the given coordinates.")

    @property
    def vertices(self):
        return self.__vertices

    def __is_member(self):
        """Returns True if number of coordinate pairs equals 4"""
        return len(self.__vertices) == 4

    def side_lengths(self):  # Distance Formula
        # sqrt((x2-x1)^2 + (y2-y1)^2)
        """Returns a tuple of four floats, each denoting the length of a side of this quadrilateral. The value must be
                ordered clockwise, starting from the top left corner."""
        one_to_zero = sqrt(((self.vertices[0].x - self.vertices[1].x) ** 2) +
                           (self.vertices[0].y - self.vertices[1].y) ** 2)
        zero_to_three = sqrt(((self.vertices[3].x - self.vertices[0].x) ** 2) +
                             (self.vertices[3].y - self.vertices[0].y) ** 2)
        three_to_two = sqrt(((self.vertices[2].x - self.vertices[3].x) ** 2) +
                            (self.vertices[2].y - self.vertices[3].y) ** 2)
        two_to_one = sqrt(((self.vertices[1].x - self.vertices[2].x) ** 2) +
                          (self.vertices[1].y - self.vertices[2].y) ** 2)

        return round(one_to_zero, 5), round(zero_to_three, 5), round(three_to_two, 5), round(two_to_one, 5)  # TODO

    def smallest_x(self):  # Go through each x and use min
        x = min(self.vertices[0].x, self.vertices[1].x)
        y = min(self.vertices[2].x, self.vertices[3].x)

        return min(x, y)

    def __eq__(self, other):
        if isinstance(other, Quadrilateral):
            return self.vertices[0].x == other.vertices[0].x and self.vertices[0].y == other.vertices[0].y and \
                   self.vertices[1].x == other.vertices[1].x and self.vertices[1].y == other.vertices[1].y and \
                   self.vertices[2].x == other.vertices[2].x and self.vertices[2].y == other.vertices[2].y and \
                   self.vertices[3].x == other.vertices[3].x and self.vertices[3].y == other.vertices[3].y
        else:
            return False

    def __str__(self):
        return "Quadrilateral:\nVertex 0:("+str(self.vertices[0].x)+", "+str(self.vertices[0].y)+")\n"+\
               "Vertex 1:("+str(self.vertices[1].x)+", "+str(self.vertices[1].y)+")\n"+\
               "Vertex 2:("+str(self.vertices[2].x)+", "+str(self.vertices[2].y)+")\n"+\
               "Vertex 3:("+str(self.vertices[3].x)+", "+str(self.vertices[3].y)+")\n"

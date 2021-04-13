# Avish Parmar 112647892
import math

from quadrilateral import Quadrilateral
from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, *floats):
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A square cannot be formed by the given coordinates.")

    def __is_member(self):
        side_lengths = self.side_lengths()

        return side_lengths[0] == side_lengths[1] == side_lengths[2] == side_lengths[3]

    def round(self, coordinate):
        fractional, y = math.modf(coordinate)

        if fractional == -.50 or fractional == .50:
            return math.ceil(coordinate)
        else:
            return round(coordinate)

    def snap(self):

        """Snaps the sides of the square such that each corner (x,y) is modified to be a corner (x',y') where x' is the
        integer value closest to x and y' is the integer value closest to y. This, of course, may change the shape to a
        general quadrilateral, hence the return type. The only exception is when the square is positioned in a way where
        this approximation will lead it to vanish into a single point. In that case, a call to snap() will not modify
        this square in any way."""

        zero = self.vertices[0]
        one = self.vertices[1]
        two = self.vertices[2]
        three = self.vertices[3]

        new_zero_x = self.round(zero.x)
        new_zero_y = self.round(zero.y)
        new_one_x = self.round(one.x)
        new_one_y = self.round(one.y)
        new_two_x = self.round(two.x)
        new_two_y = self.round(two.y)
        new_three_x = self.round(three.x)
        new_three_y = self.round(three.y)

        if new_zero_x == new_zero_y == new_one_x == new_one_y == new_two_x == new_two_y == new_three_x == new_three_y:
            raise ValueError("Square cannot be snapped since it would vanish into a single point!")

        return Quadrilateral(new_zero_x, new_zero_y, new_one_x, new_one_y,
                             new_two_x, new_two_y, new_three_x, new_three_y)  # TODO

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.vertices[0].x == other.vertices[0].x and self.vertices[0].y == other.vertices[0].y and \
                   self.vertices[1].x == other.vertices[1].x and self.vertices[1].y == other.vertices[1].y and \
                   self.vertices[2].x == other.vertices[2].x and self.vertices[2].y == other.vertices[2].y and \
                   self.vertices[3].x == other.vertices[3].x and self.vertices[3].y == other.vertices[3].y and \
                   self.area() == other.area() and self.side_lengths() == other.side_lengths() and \
                   self.center() == other.center()

    def __str__(self):
        return "Square:\nVertex 0: (" + str(self.vertices[0].x) + ", " + str(self.vertices[0].y) + ")\n" + \
               "Vertex 1: (" + str(self.vertices[1].x) + ", " + str(self.vertices[1].y) + ")\n" + \
               "Vertex 2: (" + str(self.vertices[2].x) + ", " + str(self.vertices[2].y) + ")\n" + \
               "Vertex 3: (" + str(self.vertices[3].x) + ", " + str(self.vertices[3].y) + ")\n" + \
               "Area: " + str(self.area()) + "\n" + "Center: (" + str(self.center().x) + ", " + str(
            self.center().y) + ")"
